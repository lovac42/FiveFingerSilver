@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=five_finger_silver

%ZIP% %REPO%_20.zip *.py %REPO%/*.*

cd %REPO%
%ZIP% ../%REPO%_21.zip *.*
