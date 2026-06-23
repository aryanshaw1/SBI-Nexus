from sqlalchemy import Column, Integer, String, Float

from database.connection import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    product_name = Column(
        String,
        nullable=False
    )

    confidence_score = Column(
        Float,
        nullable=False
    )

    reason = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="PENDING"
    )