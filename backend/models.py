from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, ARRAY
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    priority = Column(Integer, default=0)
    tags = Column(ARRAY(String), nullable=True)
    due_date = Column(Date, nullable=True)
    recurrence_pattern = Column(String, nullable=True)
    next_recurrence_date = Column(Date, nullable=True)
    recurrence_start_date = Column(Date, nullable=True)
    recurrence_end_date = Column(Date, nullable=True)
    reminder_time = Column(DateTime, nullable=True)
