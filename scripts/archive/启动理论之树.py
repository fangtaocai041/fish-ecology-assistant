#!/usr/bin/env python3
"""启动理论生命之树服务器"""
import http.server
import webbrowser
import os
import sys
import threading
import time
from pathlib import Path

# Change to the right directory
root = Path(__file__).parent / 'config' / 'knowledge_base' / 'ecological_theories'
os.chdir(str(root))

port = 9876

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  {args[0]}")

print(f"""
理论生命之树
════════════
  地址: http://127.0.0.1:{port}
  正在启动...""")

# Start server in background
server = http.server.HTTPServer(('127.0.0.1', port), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

time.sleep(0.5)
webbrowser.open(f'http://127.0.0.1:{port}/index.html')
print(f"  浏览器已打开")
print(f"  按 Ctrl+C 停止\n")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.shutdown()
    print("\n已停止")
