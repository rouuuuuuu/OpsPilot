from app.models.incident import Incident, IncidentCategory
from app.services.classifier import classify_incident


def make_incident(description: str) -> Incident:
    return Incident(description=description)


class TestClassifyIncident:
    def test_network_vpn(self):
        result = classify_incident(make_incident("I cannot connect to the company VPN."))
        assert result.category == IncidentCategory.NETWORK

    def test_network_wifi(self):
        result = classify_incident(make_incident("My wifi is not working."))
        assert result.category == IncidentCategory.NETWORK

    def test_account_password(self):
        result = classify_incident(make_incident("I forgot my password and cannot log in."))
        assert result.category == IncidentCategory.ACCOUNT_ACCESS

    def test_account_locked(self):
        result = classify_incident(make_incident("My account is locked after too many attempts."))
        assert result.category == IncidentCategory.ACCOUNT_ACCESS

    def test_software_crash(self):
        result = classify_incident(make_incident("The application keeps crashing on startup."))
        assert result.category == IncidentCategory.SOFTWARE

    def test_hardware_printer(self):
        result = classify_incident(make_incident("My printer is broken."))
        assert result.category == IncidentCategory.HARDWARE

    def test_unknown(self):
        result = classify_incident(make_incident("Something is wrong."))
        assert result.category == IncidentCategory.UNKNOWN

    def test_preserves_other_fields(self):
        incident = Incident(
            description="My monitor stopped working.",
            device_id="DEVICE-001",
            user_id="USER-42",
        )
        result = classify_incident(incident)
        assert result.device_id == "DEVICE-001"
        assert result.user_id == "USER-42"
        assert result.category == IncidentCategory.HARDWARE
