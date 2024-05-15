import requests

class downloadFiles:
    def __init__(self):
        pass

    def download(self, filename: str):
        response = requests.get(filename["URL"])
        if response.status_code == 200:
            with open("./arquivos/" + filename["File"], 'wb') as file:
                file.write(response.content)
            return f"Sucesso no arquivo - {filename['File']}"
        else:
            return f"Falha. Código: {response.status_code}"