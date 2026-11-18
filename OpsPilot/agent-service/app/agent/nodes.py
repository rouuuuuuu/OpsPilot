from app.models.incident import Incident
from app.services.classifier import classify_incident


def classify_incident_node(state: dict) -> dict:
    incident = Incident.model_validate(state["incident"])

    classified_incident = classify_incident(incident)

    return {
        "incident": classified_incident.model_dump(mode="json"),
        "category": classified_incident.category.value,
        "status": "classified",
    }
from app.tools.executor import execute_tool
from app.tools.handlers import TOOL_HANDLERS


async def network_diagnostics_node(state: dict) -> dict:
    device_id = state["incident"].get("device_id")

    if not device_id:
        return {
            "status": "needs_more_information",
            "response": "A device ID is required before diagnostics.",
            "diagnostic_results": [],
        }

    diagnostic_results = []

    tools_to_execute = [
        "check_vpn_status",
        "check_network_connectivity",
    ]

    for tool_name in tools_to_execute:
        result = await execute_tool(
            tool_name=tool_name,
            arguments={"device_id": device_id},
            handlers=TOOL_HANDLERS,
        )

        diagnostic_results.append(result)

    all_successful = all(
        result["success"] for result in diagnostic_results
    )

    return {
        "diagnostic_results": diagnostic_results,
        "status": (
            "diagnostics_completed"
            if all_successful
            else "diagnostics_failed"
        ),
        "response": (
            "Network diagnostics completed."
            if all_successful
            else "One or more diagnostic tools failed."
        ),
    }


def clarification_node(state: dict) -> dict:
    return {
        "status": "needs_clarification",
        "response": (
            "I couldn't confidently classify this incident. "
            "Could you provide more details?"
        ),
    }


def unsupported_category_node(state: dict) -> dict:
    return {
        "status": "awaiting_specialized_workflow",
        "response": (
            f"The {state['category']} category is recognized, "
            "but its diagnostic workflow is not implemented yet."
        ),
    }