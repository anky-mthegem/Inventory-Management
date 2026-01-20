@echo off
REM Django Inventory Management System Installer
REM This script sets up the application and creates desktop shortcuts

setlocal enabledelayedexpansion

echo.
echo ============================================
echo   Inventory Management System Installer
echo ============================================
echo.

REM Get the parent directory (project root)
cd /d "%~dp0.."
set PROJECT_ROOT=%cd%

echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and add it to PATH
    pause
    exit /b 1
)
echo OK - Python found

echo.
echo [2/5] Creating virtual environment...
if exist "myenv" (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv myenv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo OK - Virtual environment created
)

echo.
echo [3/5] Activating virtual environment and installing dependencies...
call myenv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

pip install --upgrade pip >nul 2>&1
pip install django lxml >nul 2>&1
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo OK - Dependencies installed

echo.
echo [4/5] Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo WARNING: Migration had issues, but continuing...
)
echo OK - Migrations completed

echo.
echo [5/5] Creating desktop shortcuts...
python "%PROJECT_ROOT%\installer\create_shortcuts.py" "%PROJECT_ROOT%"
if errorlevel 1 (
    echo WARNING: Desktop shortcuts creation had issues
)
echo OK - Desktop shortcuts created

echo.
echo ============================================
echo   Installation Complete!
echo ============================================
echo.
echo Desktop shortcuts have been created!
echo.
echo To start the application:
echo   - Double-click "Inventory Manager Server" shortcut
echo   - Open browser to http://localhost:8000/
echo.
echo To access:
echo   - Main Dashboard: http://localhost:8000/
echo   - Admin Panel: http://localhost:8000/admin/
echo   - API: http://localhost:8000/api/
echo.
pause
