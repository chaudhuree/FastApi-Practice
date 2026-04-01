# Running the FastAPI Practice app

Quick examples for local development.

1) Activate the virtual environment (PowerShell):

```powershell
& .\.venv\Scripts\Activate.ps1
```

2) Run using the built-in CLI runner in `main.py` (uses argparse and env defaults):

```powershell
python fastapi_01\main.py --host 0.0.0.0 --port 8000 --reload
```

You can also rely on environment variables instead of flags:

```powershell
$env:PORT = 9000
$env:RELOAD = "true"
python fastapi_01\main.py
```

3) Run with the `uvicorn` CLI directly:

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Notes:
- `--reload` is for development only (auto-restarts on file changes).
- Binding to `0.0.0.0` makes the server reachable from other hosts on your network; use `127.0.0.1` to restrict to localhost.
- For production, use a process manager (systemd, Docker, or a cloud service) and disable `--reload`.
