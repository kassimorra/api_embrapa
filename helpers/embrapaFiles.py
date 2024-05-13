class embrapaFiles:
    def __init__(self):
        #tupla
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

    def getFile(self, index):
        ret = {
            "URL" : self.files[index],
            "File" : self.files[index].replace("http://vitibrasil.cnpuv.embrapa.br/download/", "")
        }
        return ret