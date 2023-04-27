# Simples organizador de arquivos
## Quick Start
```
pip install requiments.txt
```

```python 
python3 MyFileOrganizer.py -ini
```

Isso gerará uma pasta padrão chamada downloads no seu diretório home

Se você quiser customizar a pasta de instalação rápida 

```python
python3 MyFileOrganizer -ini -dir path/para/o/diretorio
``` 
Ativará o script

```python
python3 MyFileOrganizer -w
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

Para ativar o Script digite:
```
python MyFileOrganizer.py -w
```
Para ativar sempre que ligar o computador:

Para desativar digite:

# TODO

