from sqlalchemy import Column, Integer, String

from database.connection import Base


class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    agent_name = Column(
        String,
        nullable=False
    )

    action = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="COMPLETED"
    )