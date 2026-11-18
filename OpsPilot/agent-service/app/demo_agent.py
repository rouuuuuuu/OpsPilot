import asyncio

from app.agent.graph import build_graph


async def main():
    graph = build_graph()

    initial_state = {
        "incident": {
            "description": "My office VPN is not connecting",
            "device_id": "LAPTOP-001",
            "user_id": "USER-001",
        },
        "diagnostic_results": [],
        "response": "",
    }

    result = await graph.ainvoke(initial_state)

    print("\nFinal agent state:")
    print(result)

    print("\nDiagnostic results:")

    for diagnostic in result.get("diagnostic_results", []):
        print(diagnostic)


if __name__ == "__main__":
    asyncio.run(main())