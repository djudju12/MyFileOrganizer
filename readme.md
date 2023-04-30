# Simples organizador de arquivos
## Quick Start
```
pip install requiments.txt
```

```python 
python MyFileOrganizer.py -ini
```

Isso gerará uma pasta padrão chamada downloads no seu diretório home

Voce pode passar um argumento para ini, identificando qual a pasta que será assistida

```python
python MyFileOrganizer -ini path/para/o/diretorio
``` 
Ativará o script

```python
python MyFileOrganizer -w
``` 

seu settings.json ficará na pasta que o código fonte esta instalado.

## Como utlizar
Instale os modulos  

```python
pip install requiments.txt
```

Configure as pastas e extensões que deja organizar no arquivo ```settings.json```:
```json
{
    "diretorios": {
        "C:\\seu\\diretorio\\aqui": {
            "*.mp3": "Musicas",
            "*.pdf": "Documentos",
            "*.doc": "Documentos",
            "*.odt": "Documentos",
            "*.ods": "Documentos",
            "*.jpg": "Imagens",
            "*.png": "Imagens",
            "*.csv": "Planilhas",
            "*.xlsx": "Planilhas",
            "*.zip": "Zips",
            "*.sql": "Consultas",
            "*.pls": "Consultas",
            "*.exe": "Executaveis"
        }
    }
}
```
Você pode, ou melhor, deve usar caracters coringas no arquivo de configurações, por exemplo:
```json
{
    "diretorios": {
        "C:\\seu\\diretorio\\aqui": {
            "bra[s|z]il_*": "brasil",
        }
    }
}
```
Moverá todos os arquivos que comecem com "brasil_" ou "brazil_" para pasta "brasil" 

## Para ativar o Script digite:
```
python MyFileOrganizer.py -w
```
## Para ativar sempre que ligar o computador:
###  Windows: 
 Crie um arquivo .bat e cole na sua startup folder com o seguinte comando:
  ```cmd
  python MyFileOrganizer.py -w
  ```
Acredito que seja necessário instalar o WatchDog globalmente para isso
## ! importante !
Se você chama o python de outra forma altere no ```MyFileOrganizer.py``` na variavel argumentos:

```python
ARGUMENTS = ['python', 'MyEvent.py']
# ou
ARGUMENTS = ['python3', 'MyEvent.py']
# ou
ARGUMENTS = ['py', 'MyEvent.py']
```
## Para desativar digite:
```cmd
python MyFileOrganizer.py -k 
```
# TODO

