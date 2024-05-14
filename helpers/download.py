import requests
from helpers import embrapaFiles

class downloadFiles:
    def __init__(self):
        #self.url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
        #self.save_path = "./arquivos/Producao.csv"
        pass

    def download(self, filename: str):
        response = requests.get(filename["URL"])
        if response.status_code == 200:
            with open("./arquivos/" + filename["File"], 'wb') as file:
                file.write(response.content)
            return f"Sucesso no arquivo - {filename['File']}"
        else:
            return f"Falha. Código: {response.status_code}"