from fastapi import FastAPI
from .routers import jobs
from .db import Base, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(jobs.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Scheduler Microservice Running"}
