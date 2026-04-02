@echo off
cd /d "%~dp0"
echo Philippine Law Assistant - Slim install (Python 3.14 compatible)
echo.

set "PIP_PY="
if exist "venv\Scripts\python.exe" (
  set "PIP_PY=venv\Scripts\python.exe"
  echo Using venv: %PIP_PY%
) else (
  set "PIP_PY=python"
  echo Using system Python (no venv\ found — creates packages globally for that python)
)

echo.
echo Installing Flask, flask-cors, requests...
"%PIP_PY%" -m pip install -r requirements-slim.txt

if errorlevel 1 (
  echo Installation failed.
  pause
  exit /b 1
)

echo.
echo Done! Start the backend with: start-slim.bat  (or python app_slim.py)
echo Then open http://localhost:5173 after starting the frontend.
pause
