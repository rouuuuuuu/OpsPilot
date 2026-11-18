import asyncio

from app.tools.executor import execute_tool
from app.tools.handlers import TOOL_HANDLERS


async def main():
    result = await execute_tool(
        tool_name="check_vpn_status",
        arguments={
            "device_id": "LAPTOP-001"
        },
        handlers=TOOL_HANDLERS,
    )

    print("Diagnostic result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())