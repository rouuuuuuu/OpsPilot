import asyncio
import pytest

from app.tools.executor import (
    execute_tool,
    ToolExecutionError,
)


async def successful_vpn_handler(device_id: str):
    return {
        "device_id": device_id,
        "service_status": "running",
        "diagnostic_message": "VPN service is operational",
    }


async def failing_handler(device_id: str):
    raise RuntimeError("Temporary diagnostic failure")


async def slow_handler(device_id: str):
    await asyncio.sleep(2)

    return {
        "device_id": device_id,
        "service_status": "running",
        "diagnostic_message": "VPN service is operational",
    }


async def invalid_output_handler(device_id: str):
    return {
        "device_id": device_id,
        "unexpected_field": "invalid",
    }


@pytest.mark.asyncio
async def test_successful_execution():
    result = await execute_tool(
        "check_vpn_status",
        {"device_id": "LAPTOP-001"},
        {"check_vpn_status": successful_vpn_handler},
    )

    assert result["success"] is True
    assert result["attempts"] == 1


@pytest.mark.asyncio
async def test_failed_execution():
    result = await execute_tool(
        "check_vpn_status",
        {"device_id": "LAPTOP-001"},
        {"check_vpn_status": failing_handler},
        max_attempts=2,
    )

    assert result["success"] is False
    assert result["attempts"] == 2


@pytest.mark.asyncio
async def test_timeout():
    result = await execute_tool(
        "check_vpn_status",
        {"device_id": "LAPTOP-001"},
        {"check_vpn_status": slow_handler},
        timeout_seconds=0.1,
        max_attempts=1,
    )

    assert result["success"] is False
    assert "timed out" in result["error"].lower()


@pytest.mark.asyncio
async def test_invalid_output():
    result = await execute_tool(
        "check_vpn_status",
        {"device_id": "LAPTOP-001"},
        {"check_vpn_status": invalid_output_handler},
        max_attempts=1,
    )

    assert result["success"] is False


@pytest.mark.asyncio
async def test_unknown_tool():
    with pytest.raises(ToolExecutionError):
        await execute_tool(
            "delete_database",
            {},
            {},
        )