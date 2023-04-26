import json
import os
import shutil

DIRETORIO_CONFIG = r'.\settings.json'

def move_files(path: str) -> None: 
    files = os.listdir(path)

    for file in files:
        _, file_ext = os.path.splitext(file)
        try:
            full_dir_path = os.path.join(path, DIRECTORIOS[file_ext])
        except KeyError as e:
            if file_ext != '':
                print(f'Extensao "{file_ext}" nao esta configurada')
            continue

        if not os.path.exists(full_dir_path):
            os.makedirs(full_dir_path)

        full_file_path = os.path.join(path, file)
        shutil.move(full_file_path, full_dir_path)

def write_config_file(root_dir: str, extension: str, file_dir: str) -> None:
    if not os.path.exists(DIRETORIO_CONFIG):
        new_config_file(root_dir)

    with open(DIRETORIO_CONFIG, 'r+') as f:
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

def main():
    
    rt_dir = r'C:\Users\jonathan.santos\Desktop\unisc\MyFileOrganizer\testes'
    write_config_file(rt_dir, '.odt', 'Documentos')

    
if __name__ == '__main__':
    main()
