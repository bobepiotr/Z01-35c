@echo off
ffmpeg -i %1 -ss 00:00:04.000 -vframes 1 %2
pause