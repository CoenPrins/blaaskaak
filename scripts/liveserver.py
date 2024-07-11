from http.server import HTTPServer, SimpleHTTPRequestHandler
import contextlib as context
import functools
import os
import sys
import threading
import time
from typing import NoReturn, Generator
import subprocess


def run_server(directory: str, port: int = 8000) -> None:
    handler = functools.partial(SimpleHTTPRequestHandler, directory=directory)

    try:
        server = HTTPServer(("", port), handler)
    except OSError:
        sys.exit("port already in use: is another server running?")

    print(f"Serving at http://localhost:{port}")
    with server as httpd:
        httpd.serve_forever()


def build_forever(directory: str, sleep: float = 1) -> NoReturn:
    subprocess.run(["make", "all"])
    while True:
        out = subprocess.run(["make", "site"], capture_output=True, text=True)
        if not out.stdout.startswith("make[1]: Nothing"):
            print(out.stdout)
        time.sleep(1)


if __name__ == "__main__":
    directory = "public"

    if len(sys.argv) > 1:
        directory = sys.argv[1]

    t = threading.Thread(target=run_server, args=[directory])
    t.daemon = True
    t.start()

    t2 = threading.Thread(target=build_forever, args=["."])
    t2.daemon = True
    t2.start()

    with context.suppress(KeyboardInterrupt):
        while True:
            pass
