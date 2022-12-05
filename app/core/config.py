from pydantic import BaseSettings

import os
from dotenv import load_dotenv
from typing import Any, Dict, Optional
from pydantic import PostgresDsn, validator

# Load .env file
load_dotenv()

class Settings(BaseSettings):

    main_path: str = os.path.abspath(os.path.dirname(__file__))
    routers_path: str = os.path.join(main_path, "../routers")

    ROUTER_PREFIX: str
    PROJECT_NAME: str
    SERVER_NAME: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        db_name = values.get(
            "POSTGRES_TEST_DB" if os.environ.get("PYTHON_TEST") else "POSTGRES_DB", ""
        )
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            db_name=values.get("POSTGRES_DB"),
            path=f"/{db_name}",
        )


def get_settings() -> Settings:
    return Settings(PROJECT_NAME="IN-CORE", SERVER_NAME="Maestro API")
