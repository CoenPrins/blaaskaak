from http.server import HTTPServer, SimpleHTTPRequestHandler
import contextlib as context
import functools
import os
import sys
import threading
import time
from typing import NoReturn, Generator

import buildsite


def run_server(directory: str, port: int = 8000) -> None:
    handler = functools.partial(SimpleHTTPRequestHandler, directory=directory)

    print(f"Serving at http://localhost:{port}")
    with HTTPServer(("", port), handler) as httpd:
        httpd.serve_forever()


@context.contextmanager
def suppress_stdout_stderr() -> Generator[None, None, None]:
    with open(os.devnull, "w") as devnull:
        with context.redirect_stderr(devnull), context.redirect_stdout(devnull):
            yield


def build_forever(directory: str, sleep: float = 1) -> NoReturn:
    while True:
        with suppress_stdout_stderr():
            buildsite.build(".")

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
