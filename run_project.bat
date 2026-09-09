@echo off
title SPORTX LIVE - Global Sports Stream Engine
echo =====================================================================
echo  SPORTX LIVE - Starting Clean Fresh Build...
echo =====================================================================
echo.

:: 1. Clean old port locks on 8000 and 5173
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000" ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5173" ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

:: 2. Clean Vite Cache
if exist "%~dp0frontend\node_modules\.vite" (
    rmdir /s /q "%~dp0frontend\node_modules\.vite" >nul 2>&1
)

:: 3. Detect Python (Virtual environment or System Python)
if exist "%~dp0backend\venv\Scripts\python.exe" (
    set "PYTHON_EXE=%~dp0backend\venv\Scripts\python.exe"
    echo Using Virtual Environment Python: %PYTHON_EXE%
) else (
    set "PYTHON_EXE=python"
    echo Using System Python: %PYTHON_EXE%
)

echo.
echo [1/2] Starting FastAPI Backend on http://127.0.0.1:8000 ...
start "SPORTX API Server" cmd /k "cd /d %~dp0backend && "%PYTHON_EXE%" -m uvicorn app.main:app --host 0.0.0.0 --port 8000"

timeout /t 2 /nobreak >nul

echo [2/2] Starting Vite Frontend on http://localhost:5173 ...
start "SPORTX Web Client" cmd /k "cd /d %~dp0frontend && npm run dev -- --host 0.0.0.0 --port 5173"

timeout /t 3 /nobreak >nul

:: Open browser automatically
start http://localhost:5173

echo.
echo =====================================================================
echo  SPORTX LIVE IS ONLINE!
echo  Web Platform: http://localhost:5173
echo  Backend Docs: http://127.0.0.1:8000/docs
echo =====================================================================
echo.
echo (To shut down both servers anytime, run stop_project.bat)
timeout /t 4 >nul
