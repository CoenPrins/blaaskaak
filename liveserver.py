from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess
from functools import partial

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class RebuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print("Rebuilding the project...")
        output = subprocess.run(
            ["make", "site"], shell=True, capture_output=True, text=True
        )
        if output.stderr:
            print(output.stderr)


def run_server(port=8000):
    handler = partial(SimpleHTTPRequestHandler, directory="public")

    with HTTPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    event_handler = RebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        run_server()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
