import re
from pydantic import BaseModel, field_validator


# --- Inputs ---

class DeviceInput(BaseModel):
    device_id: str

    @field_validator("device_id")
    @classmethod
    def validate_device_id(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("device_id must not be empty.")
        if not re.match(r"^[A-Za-z0-9\-_]+$", v):
            raise ValueError(
                "device_id must contain only letters, digits, hyphens, or underscores."
            )
        return v


# --- Outputs ---

class VPNStatusOutput(BaseModel):
    device_id: str
    service_status: str
    diagnostic_message: str


# Keep old name as alias for backwards compatibility
VpnStatusResult = VPNStatusOutput


class NetworkConnectivityOutput(BaseModel):
    device_id: str
    connectivity_status: str
    diagnostic_message: str


# Keep old name as alias
NetworkConnectivityResult = NetworkConnectivityOutput


class DeviceInformationOutput(BaseModel):
    device_id: str
    operating_system: str
    network_adapter_status: str


# Keep old name as alias
DeviceInformationResult = DeviceInformationOutput
