from langgraph.graph import StateGraph, START, END

from app.agent.state import OpsPilotState

from app.agent.nodes import (
    classify_incident_node,
    network_diagnostics_node,
    clarification_node,
    unsupported_category_node,
)


def route_after_classification(state: dict) -> str:
    category = state["category"]

    if category == "network":
        return "network"

    if category == "unknown":
        return "unknown"

    return "other"


def build_graph():
    workflow = StateGraph(OpsPilotState)

    # Register nodes
    workflow.add_node(
        "classify_incident",
        classify_incident_node,
    )

    workflow.add_node(
        "network_diagnostics",
        network_diagnostics_node,
    )

    workflow.add_node(
        "clarification",
        clarification_node,
    )

    workflow.add_node(
        "unsupported_category",
        unsupported_category_node,
    )

    # Starting point
    workflow.add_edge(
        START,
        "classify_incident",
    )

    # Conditional routing
    workflow.add_conditional_edges(
        "classify_incident",
        route_after_classification,
        {
            "network": "network_diagnostics",
            "unknown": "clarification",
            "other": "unsupported_category",
        },
    )

    # Ending points
    workflow.add_edge(
        "network_diagnostics",
        END,
    )

    workflow.add_edge(
        "clarification",
        END,
    )

    workflow.add_edge(
        "unsupported_category",
        END,
    )

    return workflow.compile()