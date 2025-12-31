from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth import login_user
from tasks import router as task_router

app = FastAPI(title="Task Management API with JWT")

# -------- Login --------
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(form_data)

# -------- Include Routes --------
app.include_router(task_router)
