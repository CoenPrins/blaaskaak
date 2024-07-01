from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess
from functools import partial
import threading

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class RebuildHandler(FileSystemEventHandler):
    def __init__(self, timeout):
        self.timeout = timeout
        super().__init__()
        self.timer = None

    def on_any_event(self, event):
        if self.timer:
            return
        self.timer = threading.Timer(self.timeout, self.process)
        self.timer.start()

    def process(self):
        self.timer = None
        print('rebuilding website...')
        output = subprocess.run(
            ["make", "site"], shell=True, capture_output=True, text=True
        )
        if output.stdout:
            print(output.stdout)
        if output.stderr:
            print(output.stderr)


def run_server(port=8000):
    handler = partial(SimpleHTTPRequestHandler, directory="public")

    with HTTPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    event_handler = RebuildHandler(timeout=2.0)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        run_server()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
