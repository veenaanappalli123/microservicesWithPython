# Entry point — FastAPI application.
#
# This file creates the FastAPI app instance and registers the router.
# Keep it minimal:
# - no business logic
# - no database queries
# - no repository calls
#
# The router owns the HTTP endpoints.
#
# To run locally:
#   uvicorn app.main:app --reload --port 8002
#
# Swagger:
#   http://localhost:8002/docs

from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="game-service",
    version="1.0.0"
)

# Register all HTTP routes from routes.py
app.include_router(router)


@app.get("/health")
def health():
    """
    Simple liveness endpoint used by:
    - gateway-service
    - docker/kubernetes later
    - manual debugging

    Keep this endpoint lightweight.
    """
    return {
        "status": "ok",
        "service": "game-service"
    }
