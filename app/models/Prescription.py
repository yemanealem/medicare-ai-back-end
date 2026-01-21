from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.user import User

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    prescribed_by = Column(String)
    drugs = Column(Text)
    dosage = Column(Text) 
    notes = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("User", back_populates="prescriptions")