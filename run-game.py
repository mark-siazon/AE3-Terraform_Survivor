#!/usr/bin/env python3
"""
Terraform Survivor - Game Server
Serves public frontend assets on loopback only.
"""

import webbrowser
import time
import socket
from threading import Timer
from local_game_server import HOST, create_server

PORT = 8000

def find_available_port(start_port=8000, max_attempts=10):
    """Find an available port starting from start_port"""
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, port))
                return port
        except OSError:
            continue
    return None

def open_browser(port):
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open(f'http://{HOST}:{port}/standalone.html')

if __name__ == '__main__':
    # Find an available port
    available_port = find_available_port(PORT)
    if available_port is None:
        print("❌ ERROR: Could not find an available port!")
        print(f"   Tried ports {PORT} to {PORT + 9}")
        exit(1)

    PORT = available_port

    with create_server(PORT) as httpd:
        print("=" * 60)
        print("🎮 TERRAFORM SURVIVOR - GAME SERVER")
        print("=" * 60)
        print(f"\n📡 Server running at: http://{HOST}:{PORT}")
        print("📂 Serving public src/frontend assets only (no directory listings)")
        print(f"\n🎯 PLAY THE GAME:")
        print(f"   → http://{HOST}:{PORT}/standalone.html")
        print(f"\n⚙️  Settings & Testing: Press 'O' in-game")
        print(f"\n⏹️  Press Ctrl+C to stop")
        print("=" * 60)
        print("\n🌐 Opening game in browser...\n")

        # Open browser automatically
        Timer(1.5, open_browser, args=[PORT]).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n" + "=" * 60)
            print("👋 Server stopped. Thanks for playing!")
            print("=" * 60)
