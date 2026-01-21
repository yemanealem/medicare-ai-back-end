from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DrugBase(BaseModel):
    name: str
    description: Optional[str] = None
    dosage_min: Optional[float] = None
    dosage_max: Optional[float] = None
    dosage_unit: Optional[str] = "mg"
    side_effects: Optional[str] = None
    precautions: Optional[str] = None
    interactions: Optional[str] = None
    category: Optional[str] = None


class DrugCreate(DrugBase):
    pass


class DrugUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    dosage_min: Optional[float] = None
    dosage_max: Optional[float] = None
    dosage_unit: Optional[str] = None
    side_effects: Optional[str] = None
    precautions: Optional[str] = None
    interactions: Optional[str] = None
    category: Optional[str] = None


class DrugResponse(DrugBase):
    id: int

    class Config:
        from_attributes = True
