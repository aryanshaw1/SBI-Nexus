from sqlalchemy import Column, Integer, String

from database.connection import Base


class OnboardingStatus(Base):
    __tablename__ = "onboarding_status"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    kyc_status = Column(
        String,
        default="NOT_STARTED"
    )

    application_status = Column(
        String,
        default="PENDING"
    )

    onboarding_stage = Column(
        String,
        default="PROFILE"
    )