@echo off
REM Run Inventory Management Server

cd /d "%~dp0.."
set PROJECT_ROOT=%cd%

echo.
echo ============================================
echo   Inventory Management Server
echo ============================================
echo.
echo Starting Django development server...
echo.
echo Access the application at:
echo   - Dashboard: http://localhost:8000/
echo   - Admin: http://localhost:8000/admin/
echo   - API: http://localhost:8000/api/
echo.
echo Press Ctrl+C to stop the server
echo.

call myenv\Scripts\activate.bat
python manage.py runserver

pause
