from models.user import User
from uuid import uuid4
from core.security import hash_password

def create_user(db, data):

    user = User(
        id=str(uuid4()),
        full_name=data.full_name,
        email=data.email,
        password_hash=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(db, email):
    return db.query(User).filter(
        User.email == email
    ).first()