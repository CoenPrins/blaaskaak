import http.server
import socketserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from functools import partial

DIRECTORY_TO_WATCH = "public"

class RebuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print("Rebuilding the project...")

def run_server(port=8000):
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY_TO_WATCH)
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    event_handler = RebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DIRECTORY_TO_WATCH, recursive=True)
    observer.start()

    try:
        run_server()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
