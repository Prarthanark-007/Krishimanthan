@echo off
echo ===================================================
echo   KrishiTech - Starting Django Production Server
echo ===================================================
echo.

if exist "venv\Scripts\activate.bat" (
    echo Activating Virtual Environment...
    call venv\Scripts\activate.bat
)

echo Checking/Installing Python dependencies...
python -m pip install -r requirements.txt
echo.
echo Starting the application...
echo The application will open in your default browser automatically.
start http://localhost:8000
python manage.py runserver
pause
