import json
import os
from pathlib import Path
import shutil
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

DIRETORIO_CONFIG = r'.\settings.json'

class MyEvent(FileSystemEventHandler):
    def on_any_event(self, event):
        paths_to_check = get_all_dirs(DIRETORIO_CONFIG)
        for path in paths_to_check:
            move_files(path)


def move_files(root_dir: str) -> None: 
    files = os.listdir(root_dir)

    dir_for_extesion = extesion_map(root_dir, DIRETORIO_CONFIG)

    for file in files:
        _, extension = os.path.splitext(file)
        try:
            full_dir_path = os.path.join(root_dir, dir_for_extesion[extension.lower()])
        except KeyError:
            if extension != '' or extension != '.ini':
                print(f'Extensao "{extension}" nao esta configurada')
            continue

        if path_not_exist(full_dir_path):
            os.makedirs(full_dir_path)

        full_file_path = os.path.join(root_dir, file)
        shutil.move(full_file_path, full_dir_path)

def path_not_exist(path: str):
    return not os.path.exists(path)

def extesion_map(root_dir: str, settings_dir: str):
    with open(settings_dir, 'r') as f:
        config_file = json.loads(f.read())
        diretorios = config_file['diretorios'][root_dir]
    return diretorios

def write_config_file(root_dir: str, ext: str, dir: str ) -> None:
    contents_json = read_json(DIRETORIO_CONFIG)

    with open(DIRETORIO_CONFIG, 'w') as f:
        try:
            contents_json['diretorios'][root_dir].update({ext: dir})
        except KeyError:
            contents_json['diretorios'][root_dir] = {}
            contents_json['diretorios'][root_dir].update({ext: dir})

        json.dump(contents_json, f, indent=4)
        f.truncate()

def read_json(settings_dir: str):
    with open(settings_dir, 'a+') as f:
        contents_json = f.read()
        if file_is_not_empy(f):
            print("e")
            contents_json = json.loads(f.read())
        else:          
            print("nt")
            contents_json = initial_configs(str(Path.home() / 'Downloads'))
    return contents_json

def file_is_not_empy(f):
    f.seek(0, os.SEEK_END)
    e = f.tell()
    f.seek(0)
    return e

def initial_configs(root_dir: str) -> dict:
    settings = {}
    settings['diretorios'] = {
        root_dir: { 
            '.mp3': 'Musicas',
            '.pdf': 'Documentos',
            '.doc': 'Documentos',
            '.odt': 'Documentos',
            '.ods': 'Documentos',
            '.jpg': 'Imgens',
            '.png': 'Imgens',
            '.csv': 'Planilhas',
            '.xlsx': 'Planilhas',
            '.zip': 'Zips',
            '.sql': 'Consultas',
            '.pls': 'Consultas',
            '.exe': 'Executaveis',
        }
    }
    return settings

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

def get_all_dirs(settings_path: str) -> list:
    with open(settings_path, 'r') as f:
        jsonFile = json.loads(f.read())

    return list(jsonFile['diretorios'].keys())

def main():
    write_config_file(r'C:\Users\jonathan.santos\Desktop\unisc\MyFileOrganizer\testes', '.odt', 'Documentos')
    write_config_file(r'C:\Users\jonathan.santos\Desktop\unisc\MyFileOrganizer\testes', '.pdf', 'Documentos')
    write_config_file(r'C:\Users\jonathan.santos\Desktop\unisc\MyFileOrganizer\testes', '.mp3', 'Musicas')
    write_config_file(r'C:\Users\jonathan.santos\Desktop\unisc\MyFileOrganizer\testes', '.jpg', 'Imagens')

    observe_dirs(DIRETORIO_CONFIG)

if __name__ == '__main__':
    main()
