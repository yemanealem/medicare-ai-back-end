from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Prescription, ChatMessage
from app.core.security import get_current_user
from app.services.prescription_service import validate_prescription
from app.rag.rag_service import create_prescription_rag
import uuid
from app.schemas.prescription import PrescriptionRequest


router = APIRouter(
    prefix="/api/prescriptions", 
    tags=["Prescriptions"]        
)

@router.post("/validate")
def validate_prescription(
    data: PrescriptionRequest,
    db: Session = Depends(get_db),
):
    rag = create_prescription_rag(db)

    # Convert structured data → text for LLM
    prescription_text = "\n".join([
        f"{item.drug_name} {item.dosage}{item.dosage_unit}, "
        f"{item.frequency_per_day} times per day"
        for item in data.items
    ])

    result = rag.invoke(prescription_text)

    return {
        "consultation": result.content
    }