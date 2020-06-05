@echo off
call "I:\Programs\Qgis\bin\o4w_env.bat"
call "I:\Programs\Qgis\bin\qt5_env.bat"
call "I:\Programs\Qgis\bin\py3_env.bat"

@echo on
pyrcc5 -o resources.py resources.qrc