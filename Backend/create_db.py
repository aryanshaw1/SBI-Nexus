from database.connection import Base
from database.connection import engine

from models.user import User
from models.profile import Profile
from models.lead_score import LeadScore
from models.recommendation import Recommendation
from models.onboarding_status import OnboardingStatus
from models.agent_log import AgentLog
from models.customer_journey_event import CustomerJourneyEvent
from models.analytics_snapshot import AnalyticsSnapshot

Base.metadata.create_all(bind=engine)

print("Database created successfully")