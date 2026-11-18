from app.tools.simulated_environment import SIMULATED_DEVICES


async def check_vpn_status(device_id: str):
    device = SIMULATED_DEVICES.get(device_id)

    if device is None:
        raise ValueError("Device not found")

    status = device["vpn_status"]

    return {
        "device_id": device_id,
        "service_status": status,
        "diagnostic_message": (
            "VPN service is operational"
            if status == "running"
            else "VPN service is not running"
        ),
    }


async def check_network_connectivity(device_id: str):
    device = SIMULATED_DEVICES.get(device_id)

    if device is None:
        raise ValueError("Device not found")

    status = device["connectivity_status"]

    return {
        "device_id": device_id,
        "connectivity_status": status,
        "diagnostic_message": (
            "Network connectivity is available"
            if status == "connected"
            else "Network connectivity is limited or unavailable"
        ),
    }


async def get_device_information(device_id: str):
    device = SIMULATED_DEVICES.get(device_id)

    if device is None:
        raise ValueError("Device not found")

    return {
        "device_id": device_id,
        "operating_system": device["operating_system"],
        "network_adapter_status": device["network_adapter_status"],
    }