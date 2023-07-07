from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.v1.router import router as v1_router
from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = get_application()
app.include_router(v1_router, prefix="/v1")
