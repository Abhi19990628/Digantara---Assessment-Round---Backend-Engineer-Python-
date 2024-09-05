from pydantic import BaseModel

class JobCreate(BaseModel):
    name: str
    interval: str  # Example: "Every Monday"

class Job(BaseModel):
    id: int
    name: str
    last_run: str = None
    next_run: str = None
    interval: str

    class Config:
        orm_mode = True
