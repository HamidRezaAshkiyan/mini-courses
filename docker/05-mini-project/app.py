import json
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer


def redis_incr(host: str, port: int, key: str) -> int:
    """Minimal zero-dependency Redis RESP INCR command over TCP."""
    cmd = f"*2\r\n$4\r\nINCR\r\n${len(key)}\r\n{key}\r\n".encode("utf-8")
    with socket.create_connection((host, port), timeout=3) as sock:
        sock.sendall(cmd)
        response = sock.recv(1024).decode("utf-8").strip()
    if not response.startswith(":"):
        raise RuntimeError(f"Unexpected Redis response: {response}")
    return int(response[1:])


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send_json(200, {"status": "ok"})
            return

        redis_host = os.getenv("REDIS_HOST", "redis")
        redis_port = int(os.getenv("REDIS_PORT", "6379"))
        try:
            visits = redis_incr(redis_host, redis_port, "visits")
            self._send_json(
                200,
                {
                    "visits": visits,
                    "served_by": socket.gethostname(),
                },
            )
        except OSError as exc:
            self._send_json(503, {"error": f"Redis unavailable: {exc}"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Visit Counter API listening on http://0.0.0.0:{port}", flush=True)
    server.serve_forever()
