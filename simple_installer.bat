@echo off
REM Simple installer that doesn't require InnoSetup
REM This creates a standalone setup that copies files and creates shortcuts

setlocal enabledelayedexpansion

echo.
echo ========================================
echo Django Inventory Manager Installer
echo ========================================
echo.

REM Define installation directory
set "INSTALL_DIR=%ProgramFiles%\Django Inventory Manager"

REM Create installation directory
if not exist "!INSTALL_DIR!" (
    mkdir "!INSTALL_DIR!"
    echo Created installation directory
)

REM Copy the executable
echo Copying Django Inventory Manager...
copy /Y "dist\Django_Inventory_Manager.exe" "!INSTALL_DIR!\Django_Inventory_Manager.exe" >nul

if !ERRORLEVEL! == 0 (
    echo.
    echo ========================================
    echo Installation Complete!
    echo ========================================
    echo.
    echo Location: !INSTALL_DIR!
    echo.
    echo Creating desktop shortcut...
    
    REM Create shortcut using PowerShell
    powershell -Command ^
        "$WshShell = New-Object -ComObject WScript.Shell; " ^
        "$Shortcut = $WshShell.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\Django Inventory Manager.lnk'); " ^
        "$Shortcut.TargetPath = '!INSTALL_DIR!\Django_Inventory_Manager.exe'; " ^
        "$Shortcut.WorkingDirectory = '!INSTALL_DIR!'; " ^
        "$Shortcut.Save()"
    
    echo.
    echo You can now:
    echo   1. Run from: !INSTALL_DIR!\Django_Inventory_Manager.exe
    echo   2. Use the desktop shortcut
    echo.
    echo The server will start automatically and open at http://localhost:8000
    echo.
    pause
) else (
    echo.
    echo ERROR: Installation failed!
    pause
)
