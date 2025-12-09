import os
import json
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import router as api_router
from database import create_tables
from logging_config import configure_logging

# Configure logging at the application startup
configure_logging()
logger = logging.getLogger("app")

# Default CORS origins if the environment variable is not set
DEFAULT_CORS_ORIGINS = '["http://localhost:3000"]'

# Load CORS origins from environment variable
cors_origins_str = os.environ.get("BACKEND_CORS_ORIGINS", DEFAULT_CORS_ORIGINS)

# The environment variable might be a single-quoted string, 
# so we replace single quotes with double quotes for valid JSON.
try:
    allowed_origins = json.loads(cors_origins_str.replace("'", '"'))
except json.JSONDecodeError:
    logger.warning(f"Could not parse BACKEND_CORS_ORIGINS: {cors_origins_str}. Using default.")
    allowed_origins = json.loads(DEFAULT_CORS_ORIGINS)

app = FastAPI(
    title="Todo App API",
    description="A simple API for a todo application.",
    version="0.1.0",
)

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
def on_startup():
    create_tables()

@app.get("/")
def read_root():
    """A simple health check endpoint."""
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")

# The following is a placeholder for running the app with uvicorn.
# In production, you would run this with a process manager like Gunicorn.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
