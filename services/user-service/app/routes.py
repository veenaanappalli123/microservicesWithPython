from fastapi import APIRouter, HTTPException

router = APIRouter()

fake_users = [
    {
        "id": "1",
        "username": "veena"
    }
]


@router.post("/v1/users")
def create_user():
    return {
        "message": "User created"
    }


@router.get("/v1/users")
def list_users(limit: int = 20, offset: int = 0):
    return fake_users[offset: offset + limit]


@router.get("/v1/users/{user_id}")
def get_user(user_id: str):
    for user in fake_users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
# Interface layer — HTTP endpoints.
#
# This file defines the FastAPI router and maps HTTP verbs + paths to
# service function calls. It is the only layer that knows about HTTP.
#
# Rules:
# - Never call repository functions directly — always go through service
# - Catch ValueError from the service layer and raise HTTPException instead
# - Use Depends(get_db) to inject the database session
#
# This file should expose:
# - POST   /v1/users/          -> create a user
# - GET    /v1/users/          -> list users (with limit/offset pagination)
# - GET    /v1/users/{user_id} -> get one user by ID (404 if not found)
#
# See the README for the full implementation.

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
