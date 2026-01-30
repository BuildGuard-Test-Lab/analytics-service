from fastapi import FastAPI

app = FastAPI(title="Analytics Service")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "analytics-service"}

@app.post("/api/v1/events")
def track_event(event: dict):
    return {"id": "evt_001", "status": "accepted"}

@app.get("/api/v1/reports/daily")
def daily_report():
    return {"date": "2024-01-15", "events": 15420, "unique_users": 3201}
