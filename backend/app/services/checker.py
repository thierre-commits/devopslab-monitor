import time

import httpx
from sqlalchemy.orm import Session

import threading
import time

from app.models.check import Check
from app.models.service import Service
from app.db.database import SessionLocal


def run_service_check(service: Service, db: Session) -> Check:
    start_time = time.perf_counter()

    try:
        response = httpx.get(service.url, timeout=5.0)
        response_time_ms = int((time.perf_counter() - start_time) * 1000)
        status = "up" if response.status_code < 500 else "down"

    except Exception:
        response_time_ms = int((time.perf_counter() - start_time) * 1000)
        status = "down"

    check = Check(
        service_id=service.id,
        status=status,
        response_time_ms=response_time_ms,
    )

    db.add(check)
    db.commit()
    db.refresh(check)

    return check


def run_all_service_checks(db: Session) -> list[Check]:
    services = db.query(Service).all()
    checks = []

    for service in services:
        check = run_service_check(service, db)
        checks.append(check)

    return checks

def start_scheduler(interval_seconds: int = 30):
    def loop():
        while True:
            try:
                db = SessionLocal()
                run_all_service_checks(db)
                db.close()
            except Exception as e:
                print(f"[Scheduler] error: {e}")

            time.sleep(interval_seconds)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()