@echo off
  
net session > NUL 2>NUL

if %errorLevel% == 0 (
echo ADMIN
) else (
echo NOT ADMIN
)

pause