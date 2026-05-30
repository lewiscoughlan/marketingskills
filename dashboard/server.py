#!/usr/bin/env python3
"""
CreatorHub local server.
Serves the dashboard and saves all data to data.json on your computer.
Run: python3 server.py
"""
import http.server
import json
import os
import webbrowser
import threading

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')
PORT = 8765
DIR   = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        if self.path == '/data':
            self._json_headers()
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode())
            else:
                self.wfile.write(b'null')
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(body.decode('utf-8'))
            self._json_headers()
            self.wfile.write(b'{"ok":true}')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def _json_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def log_message(self, *args):
        pass  # keep terminal clean


def open_browser():
    import time
    time.sleep(0.8)
    webbrowser.open(f'http://localhost:{PORT}')


if __name__ == '__main__':
    print(f'\n  CreatorHub is running → http://localhost:{PORT}')
    print('  Data file → data.json (same folder)')
    print('  Press Ctrl+C to stop.\n')
    threading.Thread(target=open_browser, daemon=True).start()
    with http.server.HTTPServer(('localhost', PORT), Handler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\n  Stopped.')
