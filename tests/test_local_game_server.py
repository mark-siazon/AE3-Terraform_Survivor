import http.client
from pathlib import Path
import tempfile
import threading
import unittest

from local_game_server import create_server


class LocalServerTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory()
        self.root = Path(self.fixture.name)
        self.public = self.root / "frontend"
        self.public.mkdir()
        (self.public / "index.html").write_text("public game", encoding="utf8")
        (self.public / "game.js").write_text("console.log('game')", encoding="utf8")
        (self.public / ".env").write_text("fake-private-value", encoding="utf8")
        (self.public / "private.key").write_text("fake-private-value", encoding="utf8")
        (self.public / "empty").mkdir()
        (self.root / "outside.html").write_text("outside fixture", encoding="utf8")
        self.server = create_server(0, self.public)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.fixture.cleanup()

    def request(self, target, method="GET"):
        connection = http.client.HTTPConnection(*self.server.server_address, timeout=3)
        connection.request(method, target)
        response = connection.getresponse()
        result = response.status, dict(response.getheaders()), response.read()
        connection.close()
        return result

    def test_loopback_and_public_assets(self):
        self.assertEqual(self.server.server_address[0], "127.0.0.1")
        status, headers, body = self.request("/")
        self.assertEqual((status, body), (200, b"public game"))
        self.assertNotIn("Access-Control-Allow-Origin", headers)
        self.assertEqual(self.request("/game.js")[1]["Content-type"], "application/javascript")
        self.assertEqual(self.request("/src/frontend/index.html")[0], 200)

    def test_sensitive_and_traversal_paths_are_denied(self):
        for target in ("/.env", "/.git/config", "/../outside.html", "/%2e%2e/outside.html",
                       "/%2Eenv", "/%2e%2e%5coutside.html", "/C:/outside.html", "/private.key"):
            with self.subTest(target=target):
                self.assertEqual(self.request(target)[0], 403)
                self.assertEqual(self.request(target, "HEAD")[0], 403)

    def test_directory_listing_is_denied(self):
        self.assertEqual(self.request("/empty/")[0], 403)

    def test_symlink_cannot_escape_public_root(self):
        try:
            (self.public / "escape.html").symlink_to(self.root / "outside.html")
        except OSError:
            self.skipTest("This Windows profile cannot create symlinks")
        self.assertEqual(self.request("/escape.html")[0], 403)
        hidden = self.public / ".private"
        hidden.mkdir()
        (hidden / "secret.html").write_text("fake hidden fixture", encoding="utf8")
        (self.public / "hidden.html").symlink_to(hidden / "secret.html")
        self.assertEqual(self.request("/hidden.html")[0], 403)

    def test_directory_index_symlink_cannot_bypass_public_path_checks(self):
        for name, target in (("outside-index", self.root / "outside.html"),
                             ("hidden-index", self.public / ".env")):
            directory = self.public / name
            directory.mkdir()
            try:
                (directory / "index.html").symlink_to(target)
            except OSError:
                self.skipTest("This Windows profile cannot create symlinks")
            with self.subTest(name=name):
                self.assertEqual(self.request(f"/{name}/")[0], 403)
                self.assertEqual(self.request(f"/{name}/", "HEAD")[0], 403)


if __name__ == "__main__":
    unittest.main()
