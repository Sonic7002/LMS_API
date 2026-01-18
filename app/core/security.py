import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Pre-hash to avoid bcrypt 72-byte limit
    digest = hashlib.sha256(password.encode("utf-8")).digest()
    return pwd_context.hash(digest)

def verify_password(password: str, hashed: str) -> bool:
    digest = hashlib.sha256(password.encode("utf-8")).digest()
    return pwd_context.verify(digest, hashed)
