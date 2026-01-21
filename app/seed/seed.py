from app.database import SessionLocal
from app.models import Drug

def seed_drugs():
    db = SessionLocal()
    drugs = [
        Drug(
            name="Paracetamol",
            description="Pain & fever relief",
            dosage_min=500,
            dosage_max=1000,
            dosage_unit="mg",
            side_effects="Liver toxicity in overdose",
            precautions="Avoid in liver disease",
            interactions="Alcohol",
            category="Analgesic"
        ),
        Drug(
            name="Ibuprofen",
            description="NSAID for pain and inflammation",
            dosage_min=200,
            dosage_max=400,
            dosage_unit="mg",
            side_effects="Stomach irritation, kidney issues",
            precautions="Avoid if ulcers or kidney disease",
            interactions="Other NSAIDs, anticoagulants",
            category="NSAID"
        )
    ]
    db.add_all(drugs)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_drugs()
