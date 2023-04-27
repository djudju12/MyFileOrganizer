# Simples organizador de arquivos
## Quick Start
```
pip install requiments.txt
```

```python 
python3 MyFileOrganizer.py -ini
```

Isso gerar� uma pasta padr�o chamada downloads no seu diret�rio home

Se voc� quiser customizar a pasta de instala��o r�pida 

```python
python3 MyFileOrganizer -ini -dir path/para/o/diretorio
``` 
Ativar� o script

```python
python3 MyFileOrganizer -w
``` 

seu settings.json ficar� na pasta que o c�digo fonte esta instalado.

## Como utlizar
Instale os modulos  

```python
pip install requiments.txt
```

Configure as pastas e extens�es que deja organizar no arquivo ```settings.json```:
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
Voc� pode, ou melhor, deve usar caracters coringas no arquivo de configura��es, por exemplo:
```json
{
    "diretorios": {
        "C:\\seu\\diretorio\\aqui": {
            "bra[s|z]il_*": "brasil",
        }
    }
}
```
Mover� todos os arquivos que comecem com "brasil_" ou "brazil_" para pasta "brasil" 

Para ativar o Script digite:
```
python MyFileOrganizer.py -w
```
Para ativar sempre que ligar o computador:

Para desativar digite:

# TODO

