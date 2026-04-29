from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.deps import get_db

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
        status = "ok"
    except Exception:
        db_status = "down"
        status = "error"
    
    return {
        "status": status,
        "database": db_status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
