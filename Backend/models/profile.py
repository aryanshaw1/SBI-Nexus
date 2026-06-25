from sqlalchemy import Column, Integer, String , Float

from database.connection import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    full_name = Column(
        String,
        nullable=False
    )

    occupation = Column(
        String,
        nullable=True
    )

    annual_income = Column(
        Float,
        nullable=True
    )

    risk_profile = Column(
        String,
        nullable=True
    )

    financial_goal = Column(
        String,
        nullable=True
    )