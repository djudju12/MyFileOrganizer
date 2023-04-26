# Simples organizador de arquivos
## Como utlizar
Instale o modulo WatchDog 

```python
pip install watchdog
```

Configure as pastas e extens�es que deja organizar no arquivo ```settings.json```:
```json
{
    "diretorios": {
        "C:\\seu\\diretorio\\aqui": {
            ".mp3": "Musicas",
            ".pdf": "Documentos",
            ".doc": "Documentos",
            ".odt": "Documentos",
            ".ods": "Documentos",
            ".jpg": "Imagens",
            ".png": "Imagens",
            ".csv": "Planilhas",
            ".xlsx": "Planilhas",
            ".zip": "Zips",
            ".sql": "Consultas",
            ".pls": "Consultas",
            ".exe": "Executaveis"
        }
    }
}
```

� poss�vel criar um arquivo de configura��o com algumas extens�es j� configuradas:
```powershell
python MyFileOrganizer.py --S --D "C:\seu\dir\aqui"
```

Para ativar o Script digite:
```powershell
python MyFileOrganizer.py --L
```
Para ativar sempre que ligar o computador:

Para desativar digite:

# TODO