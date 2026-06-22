from database.connection import engine
from database.base import Base

from models.user import User

Base.metadata.create_all(bind=engine)

print("Database Created Successfully")