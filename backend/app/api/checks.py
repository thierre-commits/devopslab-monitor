from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.check import Check
from app.schemas.check import CheckCreate, CheckResponse
from app.services.checker import run_all_service_checks

router = APIRouter(prefix="/checks", tags=["checks"])


@router.post("", response_model=CheckResponse)
def create_check(check: CheckCreate, db: Session = Depends(get_db)):
    new_check = Check(
        service_id=check.service_id,
        status=check.status,
        response_time_ms=check.response_time_ms,
    )

    db.add(new_check)
    db.commit()
    db.refresh(new_check)

    return new_check


@router.post("/run", response_model=list[CheckResponse])
def run_checks(db: Session = Depends(get_db)):
    return run_all_service_checks(db)


@router.get("", response_model=list[CheckResponse])
def list_checks(db: Session = Depends(get_db)):
    return db.query(Check).all()


@router.get("/service/{service_id}", response_model=list[CheckResponse])
def list_checks_by_service(service_id: int, db: Session = Depends(get_db)):
    return db.query(Check).filter(Check.service_id == service_id).all()