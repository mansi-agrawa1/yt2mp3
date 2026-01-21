from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints.yt_to_mp3 import router as yt_to_mp3_router
from app.utils.logger import get_logger
import uvicorn

logger = get_logger("main")

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)

app.include_router(
    yt_to_mp3_router,
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    logger.info("Starting server at http://127.0.0.1:8000")
