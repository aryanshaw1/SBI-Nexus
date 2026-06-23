from sqlalchemy import Column, Integer, String

from database.connection import Base


class CustomerJourneyEvent(Base):
    __tablename__ = "customer_journey_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    event_type = Column(
        String,
        nullable=False
    )

    workflow_stage = Column(
        String,
        nullable=False
    )

    event_value = Column(
        String,
        nullable=True
    )