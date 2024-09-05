from sqlalchemy import Column, Integer, String, DateTime
from .db import Base
import datetime

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_run = Column(DateTime, default=None)
    next_run = Column(DateTime, default=None)
    interval = Column(String) 
