from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(
    title="FastAPI Practice",
    description="Small example app for practicing FastAPI endpoints.",
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
    redoc_url="/redoc",
)

# Development-friendly CORS (restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Root", response_class=JSONResponse)
async def read_root(request: Request):
    base = str(request.base_url).rstrip("/")
    return {
        "message": "Server is running",
        "base": base,
        "docs": f"{base}{app.docs_url}",
        "openapi": f"{base}{app.openapi_url}",
        "redoc": f"{base}{app.redoc_url}",
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)