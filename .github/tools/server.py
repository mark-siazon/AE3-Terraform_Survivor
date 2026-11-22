#!/usr/bin/env python3
"""
Simple HTTP server for testing Terraform Survivor locally.
Serves files with proper MIME types for ES6 modules.

Usage:
    python server.py

Then open: http://localhost:8000
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from local_game_server import HOST, create_server

PORT = 8000

if __name__ == '__main__':
    with create_server(PORT) as httpd:
        print(f"🚀 Terraform Survivor Server")
        print(f"📡 Serving at: http://{HOST}:{PORT}")
        print("📂 Serving public src/frontend assets only")
        print(f"\n🎮 Open these URLs:")
        print(f"   Game entry:         http://{HOST}:{PORT}/index.html")
        print(f"   Standalone version: http://{HOST}:{PORT}/standalone.html")
        print(f"\n⏹️  Press Ctrl+C to stop\n")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
