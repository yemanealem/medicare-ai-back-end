from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.user import User

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    sender = Column(String, nullable=False)  
    message = Column(Text, nullable=False)
    session_id = Column(String, nullable=False, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("User", back_populates="chats")

User.chats = relationship("ChatMessage", order_by=ChatMessage.timestamp, back_populates="patient")
