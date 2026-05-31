import bcrypt
import jwt
import datetime
import os


# =========================
# PASSWORD HASHING
# =========================

def hash_password(password: str) -> str:

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")   # ALWAYS STORE STRING


# =========================
# PASSWORD VERIFICATION
# =========================

def verify_password(password: str, hashed_password: str) -> bool:

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")  # ALWAYS STRING → BYTES
    )


# =========================
# JWT
# =========================

SECRET = os.getenv("JWT_SECRET", "community_forum_secret")


def create_token(email):

    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")


def decode_token(token):

    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        return None