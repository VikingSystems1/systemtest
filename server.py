#!/usr/bin/env python3
"""Static file server with no-cache headers so browser always gets the latest."""
import http.server
import os

PORT = 5000

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        print(fmt % args)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with http.server.HTTPServer(("0.0.0.0", PORT), NoCacheHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
