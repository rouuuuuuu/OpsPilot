from app.tools.schemas import (
    DeviceInput,
    VPNStatusOutput,
    NetworkConnectivityOutput,
    DeviceInformationOutput,
)


TOOL_REGISTRY = {
    "check_vpn_status": {
        "description": "Checks the VPN service status of a device.",
        "input_schema": DeviceInput,
        "output_schema": VPNStatusOutput,
        "permission": "diagnostic",
        "automatic_execution": True,
    },

    "check_network_connectivity": {
        "description": "Checks network connectivity for a device.",
        "input_schema": DeviceInput,
        "output_schema": NetworkConnectivityOutput,
        "permission": "diagnostic",
        "automatic_execution": True,
    },

    "get_device_information": {
        "description": "Retrieves basic information about a device.",
        "input_schema": DeviceInput,
        "output_schema": DeviceInformationOutput,
        "permission": "diagnostic",
        "automatic_execution": True,
    },
}

