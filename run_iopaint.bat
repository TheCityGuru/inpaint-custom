@echo off
echo Starting IOPaint...
echo.
echo The application will open in your default web browser.
echo Please wait...
echo.

"%~dp0IOPaint.exe" start --model lama --device cpu --port 8080

pause
