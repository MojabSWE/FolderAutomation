from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver

import os
import time

watched_directory = "//Users/mojabjamal/Downloads"
NEW_DIR = "docs"



class MyDownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(watched_directory):
            watched_file = f"{watched_directory}/{file_name}"
            new_dest_directory = f"{watched_directory}/{NEW_DIR}"

            if not os.path.exists(new_dest_directory):
                os.mkdir(new_dest_directory)

            if file_name.endswith(".docx"):
                os.rename(watched_file, f"{new_dest_directory}/{file_name}")

if __name__ == "__main__":
    event_handler = MyDownloadHandler()
    observer = PollingObserver()
    observer.schedule(
        event_handler = event_handler, path=watched_directory, recursive = False
    )

    observer.start()
    while True:
        time.sleep(5)