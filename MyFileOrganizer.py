import fnmatch
import json
import os
from pathlib import Path
import shutil
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import argparse

DIRETORIO_CONFIG = r'settings.json'

class MyEvent(FileSystemEventHandler):
    def on_any_event(self, event):
        paths_to_check = get_all_dirs(DIRETORIO_CONFIG)
        for path in paths_to_check:
            move_files(path)


def move_files(root_dir: str) -> None: 
    files = os.listdir(root_dir)
    extension_dir_map = extesion_map(root_dir, DIRETORIO_CONFIG)

    for file in files:
        if file == '' or file == '.ini' or '.' not in file:
            continue

        valid_dir = is_file_in_settings(root_dir, extension_dir_map, file)
        if not valid_dir:
            print(f'Extensao "{file}" nao esta configurada')
            continue

        if path_not_exist(valid_dir):
            os.makedirs(valid_dir)

        full_file_path = os.path.join(root_dir, file)
        shutil.move(full_file_path, valid_dir)

def is_file_in_settings(root_dir, extensions_dir, file):
    for ext in extensions_dir.keys():
        if fnmatch.fnmatch(file, ext):
            return os.path.join(root_dir, extensions_dir[ext.lower()])
    return ""

def path_not_exist(path: str):
    return not os.path.exists(path)

def extesion_map(root_dir: str, settings_dir: str):
    with open(settings_dir, 'r') as f:
        config_file = json.loads(f.read())
        diretorios = config_file['diretorios'][root_dir]
    return diretorios

def write_config_file(root_dir=None, ext=None, dir=None) -> None:
    contents_json = read_json(DIRETORIO_CONFIG)

    with open(DIRETORIO_CONFIG, 'w') as f:
        # Se existe o diretorio e há algo para inserir entao faz
        if root_dir in contents_json:
            if all([ext, dir]):
                contents_json['diretorios'][root_dir].update({ext: dir})
        else:
            if all([ext, dir]):
                contents_json['diretorios'][root_dir] = {ext: dir}
            else:
                contents_json['diretorios'][root_dir] = initial_extesions_config(root_dir)

        # cria o json
        json.dump(contents_json, f, indent=4)
        f.truncate()

def read_json(settings_dir: str):
    with open(settings_dir, 'a+') as f:
        contents_json = f.read()

        # Retorna a estrutura do config vazia se o arquivo nao existir
        if file_is_not_empy(f):
            contents_json = json.loads(f.read())
        else:          
            contents_json = {'diretorios': {}}

    return contents_json

def file_is_not_empy(f):
    f.seek(0, os.SEEK_END)
    e = f.tell()
    f.seek(0)
    return e

def initial_extesions_config(root_dir: str) -> dict:
    return {
            '*.mp3': 'Musicas',
            '*.pdf': 'Documentos',
            '*.doc': 'Documentos',
            '*.odt': 'Documentos',
            '*.ods': 'Documentos',
            '*.jpg': 'Imagens',
            '*.png': 'Imagens',
            '*.csv': 'Planilhas',
            '*.xlsx': 'Planilhas',
            '*.zip': 'Zips',
            '*.sql': 'Consultas',
            '*.pls': 'Consultas',
            '*.exe': 'Executaveis'
        }

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
    # Retorna uma lista com os diretorios que deverão ser assitidos
    return list(jsonFile['diretorios'].keys())

def initiate_script(root_dir=None):
    if root_dir is None:
        root_dir = str(Path.home()/'Downloads')

    if path_not_exist(root_dir):
        try:
            os.mkdir(root_dir)
        except FileNotFoundError:
            print(f'Não foi possível localizar o Path => {root_dir}')
    write_config_file(root_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ini", action='store_true', help="Inicia o script")
    parser.add_argument("-dir", nargs='?', const=None)
    parser.add_argument("-w", action='store_true', help="começa a observar os diretorios")
    args = parser.parse_args()

    if args.ini:
        root_dir = args.dir 
        initiate_script(root_dir)
    
    if args.w:
        observe_dirs(DIRETORIO_CONFIG)