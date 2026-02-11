@echo off
echo ================================
echo QuickFileSearch Build Script
echo ================================

echo.
echo [1/3] Virtuelle Umgebung aktivieren...

IF EXIST venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo.
echo [2/3] Baue generate_index.exe...
python -m PyInstaller --clean --noconfirm --onefile --noconsole generate_index.pyw

echo.
echo [3/3] Baue file_viewer.exe...
python -m PyInstaller --clean --noconfirm --onefile --noconsole file_viewer.pyw

echo.
echo ================================
echo Build abgeschlossen.
echo Die EXE-Dateien befinden sich im Ordner "dist"
echo ================================
pause
