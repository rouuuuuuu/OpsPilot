from fastapi import FastAPI
from app.models.incident import Incident
from app.services.classifier import classify_incident

app = FastAPI(
    title="OpsPilot Agent Service",
    description="AI-powered IT support agent service.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/classify", response_model=Incident)
def classify(incident: Incident) -> Incident:
    """
    Receive an incident description and return it with a classified category.
    """
    return classify_incident(incident)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
