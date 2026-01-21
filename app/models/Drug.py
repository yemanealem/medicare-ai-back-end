from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Drug(Base):
    __tablename__ = "drugs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    dosage_min = Column(Float)   
    dosage_max = Column(Float)  
    dosage_unit = Column(String, default="mg")
    side_effects = Column(Text)
    precautions = Column(Text)
    interactions = Column(Text)
    category = Column(String)