import pytest

from app.tools.executor import execute_tool
from app.tools.handlers import TOOL_HANDLERS


@pytest.mark.asyncio
async def test_vpn_diagnostic():
    result = await execute_tool(
        "check_vpn_status",
        {"device_id": "LAPTOP-001"},
        TOOL_HANDLERS,
    )

    assert result["success"] is True
    assert result["output"]["service_status"] == "stopped"


@pytest.mark.asyncio
async def test_network_diagnostic():
    result = await execute_tool(
        "check_network_connectivity",
        {"device_id": "LAPTOP-003"},
        TOOL_HANDLERS,
    )

    assert result["success"] is True
    assert result["output"]["connectivity_status"] == "disconnected"


@pytest.mark.asyncio
async def test_device_information():
    result = await execute_tool(
        "get_device_information",
        {"device_id": "LAPTOP-002"},
        TOOL_HANDLERS,
    )

    assert result["success"] is True
    assert result["output"]["operating_system"] == "Ubuntu 24.04"


@pytest.mark.asyncio
async def test_unknown_device():
    result = await execute_tool(
        "check_vpn_status",
        {"device_id": "UNKNOWN-999"},
        TOOL_HANDLERS,
        max_attempts=1,
    )

    assert result["success"] is False
    assert "Device not found" in result["error"]