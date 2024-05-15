import requests
from fastapi import Response

class downloadFiles:
    def __init__(self):
        self.path = "./arquivos/"

    def download(self, filename: dict) -> str:
        response: Response = requests.get(filename["URL"])
        if response.status_code == 200:
            with open(self.path + filename["File"], 'wb') as file:
                file.write(response.content)
            return f"Sucesso no arquivo - {filename['File']}"
        else:
            return f"Falha. Código: {response.status_code}"