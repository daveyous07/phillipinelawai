@echo off
title Philippine Law Assistant - Backend
cd /d "%~dp0"

echo.
echo API: http://127.0.0.1:8000  (keep this window open)
echo.
echo LLM: default is LOCAL Ollama — no online LLM. Run: ollama serve  and  ollama pull llama3.2
echo For Google's open model locally:  set OLLAMA_MODEL=gemma3  then  ollama pull gemma3
echo Cloud Gemini only if YOU enable it:  set LLM_BACKEND=gemini  and  set GOOGLE_API_KEY=...
echo.

REM Optional overrides (uncomment):
REM set OLLAMA_MODEL=gemma3
REM set GOOGLE_API_KEY=your_key_here
REM set LLM_BACKEND=gemini


set "PY_CMD="
if exist "venv\Scripts\python.exe" set "PY_CMD=venv\Scripts\python.exe"
if defined PY_CMD goto :run

where py >nul 2>&1
if %errorlevel% equ 0 set "PY_CMD=py -3"
if defined PY_CMD goto :run

where python >nul 2>&1
if %errorlevel% equ 0 set "PY_CMD=python"

:run
if not defined PY_CMD (
  echo [ERROR] Python not found. Install Python 3 or run install-slim.bat
  pause
  exit /b 1
)

echo Using: %PY_CMD% app_slim.py
echo.
%PY_CMD% app_slim.py
if errorlevel 1 (
  echo.
  echo If imports failed, run: install-slim.bat
  pause
)
