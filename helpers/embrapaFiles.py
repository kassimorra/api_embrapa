from helpers.download import downloadFiles

class embrapaFiles:
    def __init__(self):

        self.files = (
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
        )

    def listAll(self) -> dict:
        allFiles: dict = {}
        for i in range(len(self.files)):
            allFiles[str(i)] = self.files[i].replace("http://vitibrasil.cnpuv.embrapa.br/download/", "")
        return allFiles

    def getFile(self, index: int):
        ret = {
            "URL" : self.files[index],
            "File" : self.files[index].replace("http://vitibrasil.cnpuv.embrapa.br/download/", "")
        }
        return ret
    
    def embrapaDownloadFile(self, index: int):
        downloadFile = downloadFiles()
        downloadFile.download(self.getFile(index))

    def embrapaDownloadAll(self):
        downloadFile = downloadFiles()
        for i in range(len(self.files)):
            downloadFile.download(self.getFile(i))