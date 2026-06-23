from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import DateTime

from database.connection import Base


class AnalyticsSnapshot(Base):
    __tablename__ = "analytics_snapshots"

    id = Column(String, primary_key=True)

    snapshot_date = Column(Date)

    total_leads = Column(Integer)

    conversion_rate = Column(Float)

    active_customers = Column(Integer)

    total_recommendations = Column(Integer)

    total_kyc_started = Column(Integer)

    total_kyc_completed = Column(Integer)

    top_product = Column(String)

    created_at = Column(DateTime)