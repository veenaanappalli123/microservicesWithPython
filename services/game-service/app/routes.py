from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/v1/games")

fake_games = [
    {
        "id": "1",
        "title": "Minecraft",
        "genre": "Sandbox",
        "platform": "PC",
        "cover_url": "https://example.com/minecraft.jpg"
    }
]


@router.post("/", status_code=201)
def create_game():
    return {
        "message": "Game created"
    }


@router.get("/")
def list_games(limit: int = 20, offset: int = 0):
    return fake_games[offset: offset + limit]


# IMPORTANT: /search BEFORE /{game_id}
@router.get("/search")
def search_games(q: str):
    results = []

    for game in fake_games:
        if q.lower() in game["title"].lower():
            results.append(game)

    return results


@router.get("/{game_id}")
def get_game(game_id: str):
    for game in fake_games:
        if game["id"] == game_id:
            return game

    raise HTTPException(
        status_code=404,
        detail="Game not found"
    )
# Interface layer — HTTP endpoints.
#
# Define a router with prefix="/v1/games" and implement these endpoints:
# - POST   /v1/games/          -> create a game (201)
# - GET    /v1/games/          -> list games (limit/offset pagination)
# - GET    /v1/games/search    -> search games by title (?q=...)
# - GET    /v1/games/{game_id} -> get one game by ID (404 if not found)
#
# IMPORTANT: declare /search BEFORE /{game_id} in your router.
# If /{game_id} comes first, FastAPI will try to match "search" as an ID
# and return a 422 Unprocessable Entity error.
#
# Module 5 — CQRS: also add this endpoint (declare it before /{game_id}):
# - GET /v1/games/{game_id}/summary -> read from Redis cache (404 if not cached)
#   from app.infrastructure.cache import get_game_summary

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
