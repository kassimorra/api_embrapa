from .hlpDownload import download

embrapa_urls: list[str] = [
    "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
    "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"
]

root_url: str = "http://vitibrasil.cnpuv.embrapa.br/download/"
save_path: str = "./arquivos/"

embrapa_file_list: list = [[index, url, url.replace(root_url, "")] for index, url in enumerate(embrapa_urls)]

def get_index_filename() -> dict:
    return {value[0]: value[2] for value in embrapa_file_list}

def embrapa_download_file(index: int) -> None:
    download(embrapa_file_list[index][1], save_path, embrapa_file_list[index][2])

def embrapa_download_all() -> None:
    for index in range(len(embrapa_file_list)):
        download(embrapa_file_list[index][1], save_path, embrapa_file_list[index][2])
    
def embrapa_download(index: int) -> None:
    embrapa_download_all() if index == None else embrapa_download_file(index)
