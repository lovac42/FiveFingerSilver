@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=five_finger_silver

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%/checksum.md5

quick_manifest.exe "Five Finger Silver" "2047355215" >%REPO%/manifest.json


%ZIP% %REPO%_20.zip *.py %REPO%/*.*

cd %REPO%
%ZIP% ../%REPO%_21.ankiaddon *.*
%ZIP% ../%REPO%_CCBC.adze *.*
