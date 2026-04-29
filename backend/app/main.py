from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.services import router as services_router
from app.core.config import settings
from app.core.logging import configure_logging
from app.middlewares.request_logger import RequestLoggerMiddleware

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.add_middleware(RequestLoggerMiddleware)

app.include_router(health_router)
app.include_router(services_router)