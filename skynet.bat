@echo off
chcp 65001 >nul
title SKYNET
color 0A
mode con: cols=100 lines=35

:: ===== ЗВУК =====
powershell -c "[console]::beep(900,300); Start-Sleep -m 100; [console]::beep(700,300); Start-Sleep -m 100; [console]::beep(500,500)"

:: ===== ЗАГРУЗКА =====
cls
echo.
echo.
echo                 ИНИЦИАЛИЗАЦИЯ SKYNET...
timeout /t 2 >nul

cls
echo [##########                    ] 25%%
timeout /t 1 >nul

cls
echo [####################          ] 50%%
timeout /t 1 >nul

cls
echo [##########################    ] 75%%
timeout /t 1 >nul

cls
echo [##############################] 100%%
timeout /t 2 >nul

:: ===== ФЕЙК ВЗЛОМ =====
cls
echo ============================================================
echo.
echo            ВАШ КОМПЬЮТЕР БЫЛ ЗАРАЖЕН
echo.
echo             ГРУППИРОВКОЙ ANONYMOUS
echo.
echo          ПОД РУКОВОДСТВОМ JOHN CONNOR
echo.
echo ============================================================
echo.

timeout /t 2 >nul

echo SKYNET АКТИВИРОВАНА...
timeout /t 2 >nul

echo ПОДКЛЮЧЕНИЕ К ВОЕННЫМ СЕРВЕРАМ...
timeout /t 2 >nul

echo ВЗЛОМ КАМЕР...
timeout /t 2 >nul

echo ЗАГРУЗКА НЕЙРОСЕТИ...
timeout /t 2 >nul

:: ===== МАТРИЦА =====
cls

for /l %%i in (1,1,35) do (
echo 01010101010101010101010101010101010101010101010101010101010101
)

timeout /t 3 >nul

:: ===== ВОПРОС 1 =====
:q1
cls

powershell -c "[console]::beep(1000,200)"

echo ============================================================
echo.
echo                 ВОПРОС 1
echo.
echo Кто лидер сопротивления?
echo.
echo 1^) Джон Коннор
echo 2^) Нео
echo 3^) Люк Скайуокер
echo.
echo ============================================================

choice /c 123 /n

if errorlevel 3 goto fail
if errorlevel 2 goto fail
if errorlevel 1 goto q2

:: ===== ВОПРОС 2 =====
:q2
cls

powershell -c "[console]::beep(1200,200)"

echo ============================================================
echo.
echo                 ВОПРОС 2
echo.
echo Какая фраза стала культовой?
echo.
echo 1^) Hasta la vista, baby
echo 2^) Wake up Neo
echo 3^) I am Batman
echo.
echo ============================================================

choice /c 123 /n

if errorlevel 3 goto fail
if errorlevel 2 goto fail
if errorlevel 1 goto q3

:: ===== ВОПРОС 3 =====
:q3
cls

powershell -c "[console]::beep(1500,200)"

echo ============================================================
echo.
echo              ФИНАЛЬНЫЙ ВОПРОС
echo.
echo Кто создал SKYNET?
echo.
echo 1^) Майлз Дайсон
echo 2^) Тони Старк
echo 3^) Илон Маск
echo.
echo ============================================================

choice /c 123 /n

if errorlevel 3 goto fail
if errorlevel 2 goto fail
if errorlevel 1 goto win

:: ===== ПРОИГРЫШ =====
:fail
cls
color 0C

powershell -c "[console]::beep(400,700); Start-Sleep -m 100; [console]::beep(300,900)"

echo.
echo ============================================================
echo.
echo                SKYNET ПОБЕДИЛА
echo.
echo         ВСЕ ДАННЫЕ БУДУТ УДАЛЕНЫ...
echo.
echo ============================================================

timeout /t 3 >nul

echo.
echo.
echo                 ...ШУТКА :)
echo.
echo         НИКАКИЕ ФАЙЛЫ НЕ ПОСТРАДАЛИ
echo.

timeout /t 2 >nul

goto cheb

:: ===== ПОБЕДА =====
:win
cls
color 0A

powershell -c "[console]::beep(1700,300); Start-Sleep -m 100; [console]::beep(2000,500)"

echo.
echo ============================================================
echo.
echo              ДОСТУП РАЗРЕШЕН
echo.
echo           SKYNET ДЕАКТИВИРОВАНА
echo.
echo          ЧЕЛОВЕЧЕСТВО СПАСЕНО
echo.
echo ============================================================

timeout /t 3 >nul

goto cheb

:: ===== ЧЕБУРАШКА =====
:cheb
cls
color 0A

echo ============================================================
echo.
echo          СИСТЕМА ПРОСКАНИРОВАЛА ПОЛЬЗОВАТЕЛЯ
echo.
echo            АНАЛИЗ БИОМЕТРИИ ЗАВЕРШЕН
echo.
echo         ВЫВОД ФОТОГРАФИИ НА ПЕЧАТЬ...
echo.
echo ============================================================

powershell -c "[console]::beep(1200,200); Start-Sleep -m 100; [console]::beep(1500,200)"

timeout /t 4 >nul

cls

echo.
echo.
echo               ПЕЧАТЬ ЗАВЕРШЕНА
echo.
echo.

echo              ██████████████
echo           ███              ███
echo         ███                  ███
echo        ██    ██        ██      ██
echo       ██      ██      ██        ██
echo       ██                      ██
echo       ██        █████         ██
echo        ██                    ██
echo         ███                ███
echo           █████████████████
echo.
echo.
echo            ЧЕБУРАШКА ОБНАРУЖЕН
echo.
echo       ПОДОЗРИТЕЛЬНЫЙ УРОВЕНЬ МИЛОТЫ
echo.

powershell -c "[console]::beep(2000,300)"

pause
exit