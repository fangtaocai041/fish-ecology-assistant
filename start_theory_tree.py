#!/usr/bin/env python3
"""一键启动生态学理论生命之树本地服务器"""
import http.server, webbrowser, os, sys
from pathlib import Path

root = Path(__file__).parent / 'config' / 'knowledge_base' / 'ecological_theories'
os.chdir(str(root))

port = 8765
handler = http.server.SimpleHTTPRequestHandler

print(f"""
🌳 生态学理论生命之树
═══════════════════════
  已在本地启动: http://localhost:{port}
  浏览器应该自动打开了。
  
  如果没打开，手动访问: http://localhost:{port}
  
  按 Ctrl+C 停止服务器。
""")

webbrowser.open(f'http://localhost:{port}')
http.server.HTTPServer(('', port), handler).serve_forever()
