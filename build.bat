@echo off
chcp 65001 > nul
title Akilli-Tahta-Fatihi | EXE Builder

echo ===================================================
echo   Akilli-Tahta-Fatihi | PyInstaller Derleme Betigi
echo ===================================================
echo.

:: PyInstaller kontrolu
python -m pyinstaller --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] PyInstaller bulunamadi. Yukleniyor...
    pip install pyinstaller
    echo.
)

echo [*] EXE derleme işlemi baslatiliyor, lutfen bekleyin...
echo.

pyinstaller --noconfirm --clean ^
--onefile --windowed ^
--name Akilli-Tahta-Fatihi ^
--hidden-import=tkinter ^
--hidden-import=pyautogui ^
--hidden-import=pygetwindow ^
--hidden-import=PIL ^
--hidden-import=PIL.Image ^
--hidden-import=PIL.ImageTk ^
--hidden-import=mouseinfo ^
--hidden-import=pymsgbox ^
--hidden-import=pyperclip ^
--hidden-import=pyscreeze ^
--hidden-import=pytweening ^
--add-data "assets/loading.gif;assets" ^
src/main.py

if %errorlevel% equ 0 (
    echo.
    echo ===================================================
    echo [OK] Derleme basariyla tamamlandi!
    echo [*] Çikti dosyasi: dist\Akilli-Tahta-Fatihi.exe
    echo ===================================================
) else (
    echo.
    echo ===================================================
    echo [X] Derleme sirasinda bir hata olustu.
    echo ===================================================
)

echo.
pause
