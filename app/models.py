from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime
from sqlalchemy.sql import func
from typing import Optional
from enum import Enum as PyEnum
from app.database import Base

class Priority(PyEnum):
    HIGH = 1
    MED = 2
    LOW = 3
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    priority = Column(Integer, nullable=False)
    due_date = Column(DateTime, default=func.now())
    completed = Column(Boolean, default=False)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None 
    priority: Priority
    due_date: datetime.datetime
    completed: bool = False

    class Config:
        orm_mode = True
class TaskResponse(TaskCreate):
    id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    due_date: Optional[datetime.datetime] = None
    completed: Optional[bool] = None
