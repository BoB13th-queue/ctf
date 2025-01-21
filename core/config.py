import os
from fastapi.security import OAuth2PasswordBearer
from dataclasses import dataclass, field

@dataclass
class AuthConfig:
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SECRET_KEY: str = "5b8994d916c07caaa2adf3f4d5c785bc8f0912532808806d62f4f5da375ebfa8"
    ALGORITHM: str = "HS256"
    oauth2_scheme: OAuth2PasswordBearer = field(default_factory=lambda: OAuth2PasswordBearer(tokenUrl="/auth/login"))

@dataclass
class ServerConfig:
    host: str = "0.0.0.0"
    port: int = 8000
    # workers: int = 4
    reload: bool = True # False in production This is for development only

server_config = ServerConfig()
auth_config = AuthConfig()