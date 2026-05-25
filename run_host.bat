@echo off
title ASTROVITAL MISSION CONTROL - LOCAL SERVER
color 0A

echo ================================================
echo    🚀 ASTROVITAL CC V1.0 - LOCAL SERVER
echo ================================================
echo.
echo [INFO] Starting server on local network...
echo [INFO] Anyone on same WiFi can access this app
echo.

REM === CHANGE THIS PATH TO YOUR PROJECT FOLDER ===
set "APP_PATH=D:\🛕_Jagannath_Code_Sanctum\ASTROVITAL_AI_VITALX_CORE_V1\ASTROVITAL_CC_V1"
REM =================================================

cd /d "%APP_PATH%"

if exist "%APP_PATH%\app.py" (
    echo [SUCCESS] Found app.py
    echo.
    echo [STARTING] Streamlit server...
    echo.
    streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
) else (
    echo [ERROR] app.py not found at %APP_PATH%
    echo.
    echo Please update the APP_PATH in this batch file
    pause
    exit
)

pause