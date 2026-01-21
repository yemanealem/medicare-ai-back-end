from pydantic import BaseModel
from typing import List

class PrescriptionItem(BaseModel):
    drug_name: str
    dosage: float
    dosage_unit: str
    frequency_per_day: int

class PrescriptionRequest(BaseModel):
    items: List[PrescriptionItem]
