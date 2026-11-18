from app.models.incident import Incident, IncidentCategory
import re

CATEGORY_KEYWORDS = {
    IncidentCategory.NETWORK: [
        "wifi",
        "internet",
        "vpn",
        "connection",
        "network",
        "ethernet",
        "dns",
    ],
    IncidentCategory.ACCOUNT_ACCESS: [
        "password",
        "login",
        "log in",
        "locked",
        "account",
        "authentication",
        "access denied",
    ],
    IncidentCategory.SOFTWARE: [
        "application",
        "app",
        "software",
        "crash",
        "install",
        "installation",
        "update",
        "error",
    ],
    IncidentCategory.HARDWARE: [
        "keyboard",
        "mouse",
        "screen",
        "monitor",
        "laptop",
        "printer",
        "battery",
        "hardware",
    ],
}

def classify_incident(incident: Incident) -> Incident:
    description = incident.description.lower()

    scores = {
        category: sum(
            1
            for keyword in keywords
            if re.search(r"\b" + re.escape(keyword) + r"\b", description)
        )
        for category, keywords in CATEGORY_KEYWORDS.items()
    }

    highest_score = max(scores.values())

    if highest_score == 0:
        return incident.model_copy(
            update={"category": IncidentCategory.UNKNOWN}
        )

    winners = [
        category
        for category, score in scores.items()
        if score == highest_score
    ]

    if len(winners) > 1:
        return incident.model_copy(
            update={"category": IncidentCategory.UNKNOWN}
        )

    return incident.model_copy(
        update={"category": winners[0]}
    )