import pytest

from app.tools.executor import validate_tool_request


def test_valid_tool_request():
    result = validate_tool_request(
        "check_vpn_status",
        {"device_id": "LAPTOP-001"}
    )

    assert result.device_id == "LAPTOP-001"


def test_unknown_tool():
    with pytest.raises(ValueError):
        validate_tool_request(
            "delete_company_database",
            {"device_id": "LAPTOP-001"}
        )


def test_missing_argument():
    with pytest.raises(Exception):
        validate_tool_request(
            "check_vpn_status",
            {}
        )


def test_invalid_device_id():
    with pytest.raises(Exception):
        validate_tool_request(
            "check_vpn_status",
            {"device_id": ""}
        )


def test_invalid_device_id_characters():
    with pytest.raises(Exception):
        validate_tool_request(
            "check_vpn_status",
            {"device_id": "LAPTOP 001"}
        )