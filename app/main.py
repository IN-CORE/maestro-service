from fastapi import FastAPI, APIRouter

from app.core.config import get_settings
from app.db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, roles, steps

settings = get_settings()

app = FastAPI(title=settings.SERVER_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# create tables if they don't exist - Probably shouldn't happen once alembic does the migration
Base.metadata.create_all(engine)


api_router = APIRouter()
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)
api_router.include_router(
    roles.router,
    prefix="/roles",
    tags=["roles"],
)
api_router.include_router(
    steps.router,
    prefix="/steps",
    tags=["steps"],
)

app.include_router(api_router, prefix=settings.ROUTER_PREFIX)


@app.get("/maestro")
def index():
    return {"message": "Welcome to Maestro service"}