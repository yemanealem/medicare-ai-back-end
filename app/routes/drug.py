from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.drug import DrugCreate, DrugUpdate, DrugResponse
from app.services import drug_service

router = APIRouter(
    prefix="/api/drugs",
    tags=["Drugs"]
)


@router.post("/", response_model=DrugResponse)
def create_drug(
    drug: DrugCreate,
    db: Session = Depends(get_db)
):
    return drug_service.create_drug(db, drug)


@router.get("/", response_model=List[DrugResponse])
def get_all_drugs(
    db: Session = Depends(get_db)
):
    return drug_service.get_all_drugs(db)


@router.get("/{drug_id}", response_model=DrugResponse)
def get_drug_by_id(
    drug_id: int,
    db: Session = Depends(get_db)
):
    return drug_service.get_drug_by_id(db, drug_id)


@router.put("/{drug_id}", response_model=DrugResponse)
def update_drug(
    drug_id: int,
    drug: DrugUpdate,
    db: Session = Depends(get_db)
):
    return drug_service.update_drug(db, drug_id, drug)


@router.delete("/{drug_id}")
def delete_drug(
    drug_id: int,
    db: Session = Depends(get_db)
):
    return drug_service.delete_drug(db, drug_id)
