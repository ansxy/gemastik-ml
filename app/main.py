from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.v1.router import router as v1_router

# origins = [
#             "http://localhost",
#             "http://localhost:8080",
#             "http://localhost:3000"
#         ],
def get_application():
    _app = FastAPI(title="plan_recomendations")

    _app.add_middleware(
        CORSMiddleware,
        allow_origins= ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = get_application()
app.include_router(v1_router, prefix="/api/v1")

