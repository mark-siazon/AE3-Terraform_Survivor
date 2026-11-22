"""Loopback-only static hosting for public game assets, never the repository."""

import functools
import http.server
from pathlib import Path
from urllib.parse import unquote, urlsplit


HOST = "127.0.0.1"
PUBLIC_ROOT = Path(__file__).resolve().parent / "src" / "frontend"
PUBLIC_EXTENSIONS = {".html", ".css", ".js", ".json", ".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2"}


class GameHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def _public_path(self, target):
        try:
            decoded = unquote(urlsplit(target).path).replace("\\", "/")
        except ValueError:
            return None
        # Old documentation links remain valid without exposing the repo root.
        if decoded.startswith("/src/frontend/"):
            decoded = decoded[len("/src/frontend"):]
        parts = decoded.strip("/").split("/")
        if any(part.startswith(".") or ":" in part or "\x00" in part for part in parts):
            return None
        root = Path(self.directory).resolve()
        try:
            candidate = root.joinpath(*parts).resolve()
        except (OSError, RuntimeError):
            return None
        if not candidate.is_relative_to(root):
            return None
        if any(part.startswith(".") for part in candidate.relative_to(root).parts):
            return None
        if candidate.is_file() and candidate.suffix.lower() not in PUBLIC_EXTENSIONS:
            return None
        return candidate

    def translate_path(self, target):
        candidate = self._public_path(target)
        return str(candidate) if candidate is not None else str(Path(self.directory) / "__denied__")

    def send_head(self):
        candidate = self._public_path(self.path)
        if candidate is None:
            self.send_error(403, "Only public game assets are served")
            return None
        if not candidate.is_file() and not candidate.is_dir():
            self.send_error(404, "Public asset not found")
            return None
        # SimpleHTTPRequestHandler opens directory indexes itself, so validate
        # those resolved targets too rather than letting an index symlink leak.
        if candidate.is_dir():
            directory_path = urlsplit(self.path).path.rstrip("/")
            for index in ("index.html", "index.htm"):
                if (candidate / index).is_file():
                    if self._public_path(f"{directory_path}/{index}") is None:
                        self.send_error(403, "Only public game assets are served")
                        return None
                    break
        return super().send_head()

    def list_directory(self, path):
        self.send_error(403, "Directory listings are disabled")
        return None

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def guess_type(self, target):
        if target.endswith(".js"):
            return "application/javascript"
        return super().guess_type(target)


def create_server(port=8000, directory=PUBLIC_ROOT):
    handler = functools.partial(GameHTTPRequestHandler, directory=str(directory))
    return http.server.ThreadingHTTPServer((HOST, port), handler)
