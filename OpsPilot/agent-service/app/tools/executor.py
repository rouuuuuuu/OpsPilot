import asyncio
from typing import Callable, Awaitable, Any

from pydantic import BaseModel, ValidationError

from app.tools.registry import TOOL_REGISTRY


class ToolExecutionError(Exception):
    pass


def validate_tool_request(tool_name: str, arguments: dict):
    """
    Validate that a requested tool exists and that its arguments conform to its schema.
    """
    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {tool_name}")

    tool = TOOL_REGISTRY[tool_name]
    return tool["input_schema"](**arguments)


async def execute_tool(
    tool_name: str,
    arguments: dict,
    handlers: dict[str, Callable[..., Awaitable[Any]]],
    max_attempts: int = 2,
    timeout_seconds: float = 3.0,
):
    try:
        validated_input = validate_tool_request(tool_name, arguments)
    except ValueError as exc:
        raise ToolExecutionError(str(exc)) from exc
    except ValidationError as exc:
        raise ToolExecutionError(
            f"Invalid tool arguments: {exc}"
        ) from exc

    tool = TOOL_REGISTRY[tool_name]

    if tool["automatic_execution"] is not True:
        raise ToolExecutionError(
            "Automatic execution is not permitted."
        )

    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")

    if tool_name not in handlers:
        raise ToolExecutionError(
            f"No handler registered for {tool_name}"
        )

    handler = handlers[tool_name]

    for attempt in range(1, max_attempts + 1):
        try:
            raw_output = await asyncio.wait_for(
                handler(**validated_input.model_dump()),
                timeout=timeout_seconds,
            )

            validated_output = tool["output_schema"].model_validate(
                raw_output
            )

            return {
                "success": True,
                "tool_name": tool_name,
                "attempts": attempt,
                "output": validated_output.model_dump(),
                "error": None,
            }

        except asyncio.TimeoutError:
            error_message = "Tool execution timed out."

        except Exception as exc:
            error_message = str(exc)

        if attempt == max_attempts:
            return {
                "success": False,
                "tool_name": tool_name,
                "attempts": attempt,
                "output": None,
                "error": error_message,
            }