from enum import Enum
from pydantic import BaseModel


class IncidentCategory(str, Enum):
    NETWORK = "network"
    ACCOUNT_ACCESS = "account_access"
    SOFTWARE = "software"
    HARDWARE = "hardware"
    UNKNOWN = "unknown"


class Incident(BaseModel):
    description: str
    category: IncidentCategory = IncidentCategory.UNKNOWN
    device_id: str | None = None
    user_id: str | None = None
    additional_context: str | None = None
