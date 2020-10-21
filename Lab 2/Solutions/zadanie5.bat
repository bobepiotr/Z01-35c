@echo off
ffmpeg -i %1 -ss 00:00:04.000 -vframes 1 C:\Users\Piotrek\thumbnail.jpg
pause