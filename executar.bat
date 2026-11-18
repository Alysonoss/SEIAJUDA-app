@echo off
title SEI Guia
python main.py
if errorlevel 1 (
    echo.
    echo O SEI Guia encontrou um erro ao iniciar.
    echo Leia a mensagem exibida acima para identificar a causa.
    echo.
    pause
)
