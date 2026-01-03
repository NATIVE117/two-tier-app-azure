from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import logging
import sys
import uuid

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

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    return response

# Allow frontend to call backend (tighten later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(request: Request):
    logger.info(
        f"request_id={request.headers.get('x-request-id','')} "
        f"path={request.url.path} method={request.method} root endpoint hit"
    )
    return {"message": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/message")
async def message(request: Request):
    logger.info(
        f"request_id={request.headers.get('x-request-id','')} "
        f"path={request.url.path} method={request.method} message endpoint hit"
    )
    return {"message": "Hello from the backend API (Docker on Azure App Service)."}
