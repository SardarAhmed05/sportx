@echo off
title SPORTX LIVE - Shutdown Engine
echo =====================================================================
echo  SPORTX LIVE - Stopping All Servers...
echo =====================================================================
echo.

:: 1. Kill any process listening on 8000
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000" ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

:: 2. Kill any process listening on 5173
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5173" ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

:: 3. Clean any remaining python/node dev processes
taskkill /F /IM uvicorn.exe >nul 2>&1

echo [OK] All SPORTX servers have been stopped.
echo Ports 8000 and 5173 are now free.
timeout /t 2 >nul
