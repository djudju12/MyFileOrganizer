from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from MyFileOrganizer import *
import time

class MyEvent(FileSystemEventHandler):
    def on_any_event(self, event):
        paths_to_check = get_all_dirs(DIRETORIO_CONFIG)
        for path in paths_to_check:
            move_files(path)


def observe_dirs(settings_path: str):
    event_handler = MyEvent()
    observer = Observer()
    paths = get_all_dirs(settings_path)
    observers = []

    for path in paths:
        observer.schedule(event_handler, path, recursive=False)
        observers.append(observer)
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        for o in observers:
            o.stop()
            o.join()

if __name__ == '__main__':
    observe_dirs(DIRETORIO_CONFIG)