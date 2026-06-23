from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base

class LeadScore(Base):
    __tablename__ = "lead_scores"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    score = Column(Integer)

    category = Column(String)

    persona = Column(String)