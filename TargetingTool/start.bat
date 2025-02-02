@echo off
REM Переход в корень диска D
D:
cd D:\Work\TargetingTool

REM Активация виртуального окружения
call venv\Scripts\activate.bat  # Было: venvScripts\...

REM Запуск скрипта
python src\launcher.py

echo Текущая директория: %cd%  # Было: Жеб%
dir src

pause
