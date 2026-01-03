from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging
import sys

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(name)s %(message)s'
)
handler.setFormatter(formatter)

# Avoid duplicate handlers if the module reloads
if not logger.handlers:
    logger.addHandler(handler)

app = FastAPI(title="Two-Tier API")

# Allow frontend to call backend (tighten later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    logger.info("root endpoint hit")
    return {"message": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/message")
def message():
    logger.info("message endpoint hit")
    return {"message": "Hello from the backend API (Docker on Azure App Service)."}
