@echo off
echo Starting Inpaint...
echo.
echo The application will open in your default web browser.
echo Please wait...
echo.

"%~dp0Inpaint.exe" start --model lama --device cpu --port 8080

pause
