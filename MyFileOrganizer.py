import fnmatch
from io import TextIOWrapper
import json
import os
from pathlib import Path
import shutil
import subprocess
import argparse
import psutil

DIRETORIO_CONFIG = r'/home/jonathan/programacao/MyFileOrganizer/settings.json'
ARGUMENTS = ['python3', r'/home/jonathan/programacao/MyFileOrganizer/MyEvent.py']
INITIAL_CONFIG = {
    "*.mp3" : "Musicas",
    "*.pdf" : "Documentos",
    "*.doc" : "Documentos",
    "*.docx": "Documentos",
    "*.odt" : "Documentos",
    "*.ods" : "Documentos",
    "*.jpeg": "Imagens",
    "*.jpg" : "Imagens",
    "*.png" : "Imagens",
    "*.csv" : "Planilhas",
    "*.xlsx": "Planilhas",
    "*.zip" : "Zips",
    "*.sql" : "Consultas",
    "*.pls" : "Consultas",
    "*.exe" : "Executaveis"
}
PID_DIR = r'/home/jonathan/programacao/MyFileOrganizer/pid.txt'

def move_files(root_dir: str) -> None: 
    files = os.listdir(root_dir)
    extension_dir_map = extesion_map(root_dir, DIRETORIO_CONFIG)

    for file in files:
        if not_valid_file(file):
            continue

        valid_dir = is_file_in_settings(root_dir, extension_dir_map, file)
        if not valid_dir:
            print(f'Extensao "{file}" nao esta configurada')
            continue

        if path_not_exist(valid_dir):
            os.makedirs(valid_dir)

        try:
            full_file_path = os.path.join(root_dir, file)
            shutil.move(full_file_path, valid_dir)
        except shutil.Error:
            file = '(copy) ' + file
            new_path = os.path.join(root_dir, file)
            os.rename(full_file_path, new_path)
            shutil.move(new_path, valid_dir)

def not_valid_file(file):
    invalids_formats = ['*.ini', '', '*.crdownload', '*.temp']
    if file_is_folder(file):
        return True
    for format in invalids_formats:
        if fnmatch.fnmatch(file, format):
            return True
    return False

def file_is_folder(file):
    return not fnmatch.fnmatch(file, '*.*')

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
        if file_is_not_empty(f):
            contents_json = json.loads(f.read())
        else:          
            contents_json = {'diretorios': {}}

    return contents_json

def file_is_not_empty(f):
    if isinstance(f, str): # path
        if path_not_exist(f):
            return False
        with open(f, 'r') as file:
            return file_is_not_empty(file)
    
    if isinstance(f, TextIOWrapper):
        f.seek(0, os.SEEK_END)
        e = f.tell()
        f.seek(0)
    return e

def file_is_empty(f):
    return not file_is_not_empty(f)

def initial_extesions_config(root_dir: str) -> dict:
    return INITIAL_CONFIG

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

def run_new_process():
    proc = subprocess.Popen(ARGUMENTS)
    with open(PID_DIR, 'w') as f:
        f.write(str(proc.pid))
    print(f'process is now running. Pid => {proc.pid}')

def is_process_runing(pid: int):
    return psutil.pid_exists(pid)

def pid_from_file():
    with open(PID_DIR, 'r') as f:
        pid = int(f.read().strip())
    return pid

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        print(f'process is now killed. Pid => {pid}')
        proc.terminate()
    except psutil.NoSuchProcess:
        print('process is already dead')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ini", nargs='?',default=False, help="Inicia o script")
    parser.add_argument("-w", action='store_true', help="começa a observar os diretorios")
    parser.add_argument("-k", action='store_true', help="mata o processo que assiste os diretorios")
    args = parser.parse_args()

    if args.ini or args.ini is None :
        initiate_script(args.ini)

    if args.w:
        if path_not_exist(PID_DIR):
            run_new_process()
        else:
            if file_is_not_empty(PID_DIR):
                if is_process_runing(pid_from_file()):
                    print('process is already running')
                else:
                    run_new_process()
            else:
                run_new_process()

    if args.k:
        if file_is_empty(PID_DIR) or path_not_exist(PID_DIR):
            print('nothing to kill')
        else:
            kill_process(pid_from_file())

if __name__ == '__main__':
    main()
