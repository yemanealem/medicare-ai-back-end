from app.models import Drug, Prescription
from sqlalchemy.orm import Session

def validate_prescription(db: Session, prescription: Prescription):
    """
    Validate dosage ranges and drug existence.
    Returns a list of issues, empty if safe.
    """
    issues = []
    drug_names = [d.strip() for d in prescription.drugs.split(",")]
    dosages = [float(d.strip().replace("mg", "")) for d in prescription.dosage.split(",")]

    for i, drug_name in enumerate(drug_names):
        drug = db.query(Drug).filter(Drug.name.ilike(drug_name)).first()
        if not drug:
            issues.append(f"Drug {drug_name} not found in clinical reference.")
            continue
        dose = dosages[i]
        if dose < drug.dosage_min or dose > drug.dosage_max:
            issues.append(f"{drug.name} dosage {dose}{drug.dosage_unit} is outside safe range ({drug.dosage_min}-{drug.dosage_max}{drug.dosage_unit}).")

    return issues
