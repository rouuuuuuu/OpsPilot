from typing import TypedDict


class OpsPilotState(TypedDict, total=False):
    incident: dict

    category: str

    diagnostic_results: list[dict]

    status: str

    response: str