from app.tools.diagnostics import (
    check_vpn_status,
    check_network_connectivity,
    get_device_information,
)


TOOL_HANDLERS = {
    "check_vpn_status": check_vpn_status,
    "check_network_connectivity": check_network_connectivity,
    "get_device_information": get_device_information,
}