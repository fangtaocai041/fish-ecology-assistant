@echo off
chcp 65001 >nul
cd /d "%~dp0config\knowledge_base\ecological_theories"
echo.
echo   🌳 生态学理论生命之树
echo   ══════════════════════
echo   正在启动本地服务器...
echo   浏览器将自动打开 http://localhost:9876
echo   按 Ctrl+C 停止
echo.
start http://localhost:9876
python -m http.server 9876
pause
