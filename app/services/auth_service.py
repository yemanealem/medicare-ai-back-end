from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate) -> User:
    # Check if username or email exists
    if db.query(User).filter((User.username == user.username) | (User.email == user.email)).first():
        raise ValueError("Username or email already exists")

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        phone_number=user.phone_number,
        age=user.age,
        gender=user.gender
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
