@echo off
title SEI Guia
python main.py
if errorlevel 1 (
    echo.
    echo Nao foi possivel iniciar o SEI Guia.
    echo Verifique se o Python e o PySide6 estao instalados.
    echo.
    pause
)
