from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import argparse

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


def main():
    parser = argparse.ArgumentParser(description="Run the FastAPI app with uvicorn")
    parser.add_argument("--host", default=os.environ.get("HOST", "0.0.0.0"), help="Host to bind to")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8000)), help="Port to listen on")
    default_reload = os.environ.get("RELOAD", "true").lower() in ("1", "true", "yes")
    parser.add_argument("--reload", action="store_true", default=default_reload, help="Enable auto-reload (dev)")
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port, reload=args.reload)


if __name__ == "__main__":
    main()