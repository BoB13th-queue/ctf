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
    host: str = os.getenv("HOST")
    port: int = int(os.getenv("PORT"))
    # workers: int = int(os.getenv("WORKERS", 4))
    reload: bool = True # False in production This is for development only

server_config = ServerConfig()
auth_config = AuthConfig()