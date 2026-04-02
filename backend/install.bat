@echo off
echo Adding Cargo to PATH for this session...
set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"

echo.
echo Checking for Cargo...
cargo --version
if errorlevel 1 (
    echo ERROR: Cargo not found. Install Rust from https://rustup.rs first.
    pause
    exit /b 1
)

echo.
echo Installing Python dependencies...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation failed. Try using Python 3.12 instead:
    echo   py -3.12 -m venv venv
    echo   venv\Scripts\activate
    echo   python -m pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo Done! Start the backend with: python -m uvicorn app.main:app --reload --port 8000
pause
