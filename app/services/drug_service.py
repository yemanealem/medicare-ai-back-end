from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.Drug import Drug
from app.schemas.drug import DrugCreate, DrugUpdate


def create_drug(db: Session, drug_data: DrugCreate) -> Drug:
    existing = db.query(Drug).filter(Drug.name == drug_data.name).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Drug with this name already exists"
        )

    drug = Drug(**drug_data.model_dump())
    db.add(drug)
    db.commit()
    db.refresh(drug)
    return drug


def get_all_drugs(db: Session):
    return db.query(Drug).all()


def get_drug_by_id(db: Session, drug_id: int) -> Drug:
    drug = db.query(Drug).filter(Drug.id == drug_id).first()
    if not drug:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Drug not found"
        )
    return drug


def update_drug(db: Session, drug_id: int, drug_data: DrugUpdate) -> Drug:
    drug = get_drug_by_id(db, drug_id)

    for field, value in drug_data.model_dump(exclude_unset=True).items():
        setattr(drug, field, value)

    db.commit()
    db.refresh(drug)
    return drug


def delete_drug(db: Session, drug_id: int):
    drug = get_drug_by_id(db, drug_id)
    db.delete(drug)
    db.commit()
    return {"message": "Drug deleted successfully"}
