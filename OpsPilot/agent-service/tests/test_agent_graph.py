import pytest

from app.agent.graph import build_graph


@pytest.mark.asyncio
async def test_network_incident_runs_diagnostics():
    graph = build_graph()

    state = {
        "incident": {
            "description": "My office VPN is not connecting",
            "device_id": "LAPTOP-001",
        }
    }

    result = await graph.ainvoke(state)

    assert result["category"] == "network"
    assert result["status"] == "diagnostics_completed"
    assert len(result["diagnostic_results"]) == 2


@pytest.mark.asyncio
async def test_unknown_incident_requests_clarification():
    graph = build_graph()

    state = {
        "incident": {
            "description": "Something strange is happening",
        }
    }

    result = await graph.ainvoke(state)

    assert result["category"] == "unknown"
    assert result["status"] == "needs_clarification"


@pytest.mark.asyncio
async def test_software_incident_uses_other_route():
    graph = build_graph()

    state = {
        "incident": {
            "description": "My application keeps crashing",
        }
    }

    result = await graph.ainvoke(state)

    assert result["category"] == "software"
    assert result["status"] == "awaiting_specialized_workflow"


@pytest.mark.asyncio
async def test_network_incident_without_device_id():
    graph = build_graph()

    state = {
        "incident": {
            "description": "My office VPN is not connecting",
        }
    }

    result = await graph.ainvoke(state)

    assert result["status"] == "needs_more_information"
    assert result["diagnostic_results"] == []