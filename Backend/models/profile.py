from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database.base import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(String)

    occupation = Column(String)

    income = Column(String)

    risk_profile = Column(String)

    investment_goal = Column(String)