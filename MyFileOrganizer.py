import json
import os
import shutil
import time

DIRETORIO_CONFIG = r'.\settings.json'

def move_files(root_dir: str) -> None: 
    files = os.listdir(root_dir)

    with open(DIRETORIO_CONFIG, 'r') as f:
        config_file = json.loads(f.read())
        diretorios = config_file['diretorios'][root_dir]

    for file in files:
        _, file_ext = os.path.splitext(file)
        try:
            full_dir_path = os.path.join(root_dir, diretorios[file_ext])
        except KeyError:
            if file_ext != '':
                print(f'Extensao "{file_ext}" nao esta configurada')
            continue

        if not os.path.exists(full_dir_path):
            os.makedirs(full_dir_path)

        full_file_path = os.path.join(root_dir, file)
        shutil.move(full_file_path, full_dir_path)

def write_config_file(root_dir: str, extension: str, file_dir: str) -> None:
    if not os.path.exists(DIRETORIO_CONFIG):
        new_config_file(root_dir)

    with open(DIRETORIO_CONFIG, 'r+') as f:
        try:
            contents_json = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            new_config_file(root_dir)
            contents_json = json.loads(f.read())

        contents_json['diretorios'][root_dir][extension] = file_dir
        f.seek(0)
        json.dump(contents_json, f)
        f.truncate()

def new_config_file(root_dir: str) -> None:
    settings = {}
    settings['diretorios'] = {
        root_dir: { 
            '.mp3': 'Musicas',
            '.pdf': 'Documentos',
            '.jpg': 'Imgens'
        }
    }

    with open(DIRETORIO_CONFIG, 'w') as j:
        j.write(json.dumps(settings))

def teste():
    root_dir = r'C:\Users\jonathan.santos\Desktop\unisc\MyFileOrganizer\testes'
    write_config_file(root_dir, '.odt', 'Documentos')
    move_files(root_dir)

def observe_dirs(settings_path: str):
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer

    class MyEvent(FileSystemEventHandler):
        def on_modified(self, event):
            teste()
    
    event_handler = MyEvent()
    observer = Observer()

    with open(settings_path, 'r') as f:
        jsonFile = json.loads(f.read())
    
    paths = jsonFile['diretorios'].keys()
    observers = []
    print(paths[0])
    for path in paths:
        observer.schedule(event_handler, path)
        observers.append(observer)
    
    observer.start()

    try:
        while True:
            time.sleep(1)
    finally:
        for o in observers:
            o.stop()
            o.join()

def main():
    observe_dirs(DIRETORIO_CONFIG)


    
if __name__ == '__main__':
    main()
