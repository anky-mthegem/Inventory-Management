@echo off
REM This script builds the InnoSetup installer
REM Make sure Inno Setup is installed (from https://jrsoftware.org/isinfo.php)

echo.
echo Building Django Inventory Manager Installer...
echo.

REM Check if Inno Setup is installed
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" Django_Inventory_Manager.iss
    if %ERRORLEVEL% == 0 (
        echo.
        echo SUCCESS! Installer created at: dist\installer\Django_Inventory_Manager_Setup.exe
        echo.
        pause
    ) else (
        echo ERROR: Failed to create installer
        pause
    )
) else (
    echo ERROR: Inno Setup not found at default location
    echo Please install Inno Setup from: https://jrsoftware.org/isinfo.php
    echo Then run this script again
    pause
)
