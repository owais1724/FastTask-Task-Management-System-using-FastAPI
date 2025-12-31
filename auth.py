from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta

# ---------------- CONFIG ----------------
SECRET_KEY = "CHANGE_THIS_SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ---------------- FAKE USERS ----------------
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "username": "user",
        "password": "user123",
        "role": "customer"
    }
}

# ---------------- JWT UTILS ----------------
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )


def admin_only(user=Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access only")
    return user


# ---------------- LOGIN ROUTE ----------------
def login_user(form_data: OAuth2PasswordRequestForm):
    user = fake_users_db.get(form_data.username)

    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": user["username"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }
