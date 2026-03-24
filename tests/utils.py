import os
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional

def generate_salt() -> str:
    return secrets.token_hex(16)

def hash_password(password: str, salt: str) -> str:
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    hasher.update(salt.encode('utf-8'))
    return hasher.hexdigest()

def verify_password(password: str, salt: str, hashed_password: str) -> bool:
    return hash_password(password, salt) == hashed_password

def generate_token() -> str:
    return secrets.token_urlsafe(32)

def is_token_expired(created_at: datetime, expires_in: int) -> bool:
    return datetime.utcnow() > created_at + timedelta(seconds=expires_in)

def ensure_directory_exists(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def load_env_variable(key: str, default: Optional[str] = None) -> str:
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set.")
    return value