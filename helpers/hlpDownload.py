import requests
from fastapi import Response

def download(url: str, savePath: str, fileName: str) -> str:
    response: Response = requests.get(url)
    if response.status_code == 200:
        with open(savePath + fileName, 'wb') as file:
            file.write(response.content)
        return f"Sucesso no arquivo - {fileName}"
    else:
        return f"Falha. Código: {response.status_code}"