import os
from fastapi.security import OAuth2PasswordBearer
from dataclasses import dataclass, field

@dataclass
class AuthConfig:
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    oauth2_scheme: OAuth2PasswordBearer = field(default_factory=lambda: OAuth2PasswordBearer(tokenUrl="/auth/login"))

@dataclass
class ServerConfig:
    def __init__(self, mode: str = "PROD"):
        self.host: str = os.getenv("HOST")
        self.port: int = int(os.getenv("PORT"))

        if mode == "DEV":
            self.reload = True
        else:
            self.workers: int = int(os.getenv("WORKERS", os.cpu_count() * 2 + 1))

server_config = ServerConfig(os.getenv("MODE", "PROD"))
auth_config = AuthConfig()