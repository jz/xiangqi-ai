#!/usr/bin/env python3
"""静态服务器：带 COOP/COEP 响应头（多线程 WASM 需要 SharedArrayBuffer）"""
import mimetypes
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8766
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("application/octet-stream", ".nnue")


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    print(f"对弈地址: http://localhost:{PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
