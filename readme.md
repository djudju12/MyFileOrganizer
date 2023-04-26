# Simples organizador de arquivos
## Como utlizar
Instale o modulo WatchDog 

```python
pip install watchdog
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

É possível criar um arquivo de configuração com algumas extensões já configuradas:
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