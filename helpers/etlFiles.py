import pandas as pd
import os
import re
from unidecode import unidecode
from .hlpEmbrapa import embrapa_download_file,embrapa_download_all

class etlFiles:
    def __init__(self):
        self.pathFiles = (
            "arquivos/Producao.csv",
            "arquivos/ProcessaViniferas.csv",
            "arquivos/ProcessaAmericanas.csv",
            "arquivos/ProcessaMesa.csv",
            "arquivos/ProcessaSemclass.csv",
            "arquivos/Comercio.csv",
            "arquivos/ImpVinhos.csv",
            "arquivos/ImpEspumantes.csv",
            "arquivos/ImpFrescas.csv",
            "arquivos/ImpPassas.csv",
            "arquivos/ImpSuco.csv",
            "arquivos/ExpVinho.csv",
            "arquivos/ExpEspumantes.csv",
            "arquivos/ExpUva.csv",
            "arquivos/ExpSuco.csv"
        )
        self.path2SaveEtl = "arquivosEtl/"
        self.allFilesList = []
        self.file = pd.DataFrame
        self.dictCol = {
                        "id" : int,
                        "control" : str,
                        "produto" : str,
                        "pais" : str,
                        "cultivar" : str
                        }
        
    def readAllFiles(self,index):
        if(index == -1):
            try:
                embrapa_download_all()
                pathVerify = self.pathFiles[0].split("/")[0]
                if(len(os.listdir(pathVerify)) != 0):
                    for file in self.pathFiles:
                        if(file.find("Processa") == -1):
                            self.allFilesList.append(pd.read_csv(file, sep=";"))
                        else:
                            self.allFilesList.append(pd.read_csv(file, sep="\t"))
                else:
                    raise ValueError("Falha na leitura dos arquivos")
            except:
                raise ValueError("Falha ao baixar arquivos")
            
        else:
            try:
                embrapa_download_file(index)
                if(os.path.isfile(self.pathFiles[index])):
                    path = self.pathFiles[index]
                    if(path.find("Processa") == -1):
                        self.file = pd.read_csv(path, sep=";")
                    else:
                        self.file = pd.read_csv(path, sep="\t")
                else:
                    raise ValueError("Falha na leitura do arquivo")
            except:
                raise ValueError("Falha ao baixar arquivo individual")
            
    def returnAllFiles(self):
        return self.allFilesList
    
    def returnFile(self):
        return self.file

    def subNoneAsZero(self, index):
        if(index == -1):
            if (len(self.allFilesList) != 0):
                for i, file in enumerate(self.allFilesList):
                    self.allFilesList[i] = self.allFilesList[i].fillna(0)
            else:
                raise ValueError("Falha ao retirar valores nulos")
        else:
            self.file = self.file.fillna(0)
        
    
    def clearNullValues(self,index):
        if(index == -1):
            if (len(self.allFilesList) != 0):
                for i, file in enumerate(self.allFilesList):
                    self.allFilesList[i] = self.allFilesList[i].dropna()
            else:
                raise ValueError("Falha ao retirar valores nulos")
        else:
            self.file = self.file.dropna()
    
    def removeDuplicates(self,index):
        if(index == -1):
            if (len(self.allFilesList) != 0):
                for i, file in enumerate(self.allFilesList):
                    self.allFilesList[i] = self.allFilesList[i].drop_duplicates()
            else:
                raise ValueError("Falha ao remover duplicatas")
        else:
            self.file = self.file.drop_duplicates()

    def ajustTypes(self,index):
        if(index == -1):
            if (len(self.allFilesList) != 0):
                for i, file in enumerate(self.allFilesList):
                    file.rename(columns=self.ajustNameColumns, inplace=True)
                    for col in file.columns:
                        if(col in self.dictCol):
                            file[col] = file[col].astype(self.dictCol.get(col))
                        else:
                            file[col].infer_objects()
            else:
                raise ValueError("Falha ao salvar arquivos")
        else:
            self.file.rename(columns=self.ajustNameColumns, inplace=True)
            for col in self.file.columns:
                if(col in self.dictCol):
                    self.file[col] = self.file[col].astype(self.dictCol.get(col))
                else:
                    self.file[col].infer_objects()
                
            
        
    def ajustNameColumns(self,col):
        colSemAcento = unidecode(col)
        return colSemAcento.lower()
        
    def ajustNameColumnsNumbs(self,df):
        struct2Find = r"\b\d+\.\d+\b"
        for col in df:
            if(re.findall(struct2Find,col)):
                newName = col.split(".")[0]
                col = df.rename(columns={col: newName}, inplace=True)
        return df
            
    def sumSameColuns(self,index):
        #Necessidade verifciar caso index não conhecida entre as colunas, como fica
        if(index == -1):
            if (len(self.allFilesList) != 0):
                for i, file in enumerate(self.allFilesList):
                    file = self.ajustNameColumnsNumbs(file)
                    duplicatedColumns = file.columns[file.columns.duplicated()]
                    for col in duplicatedColumns:
                        dfMiddle = file[col].sum(axis=1)
                        file.drop(col, axis=1, inplace=True)
                        file[col] = dfMiddle
            else:
                raise ValueError("Falha ao remover duplicatas")
        else:
            self.file = self.ajustNameColumnsNumbs(self.file)
            duplicatedColumns = self.file.columns[self.file.columns.duplicated()]
            for col in duplicatedColumns:
                dfMiddle = self.file[col].sum(axis=1)
                self.file.drop(col, axis=1, inplace=True)
                self.file[col] = dfMiddle
            

    def saveFiles(self,index):
        if(index == -1):
            if (len(self.allFilesList) != 0):
                for i, file in enumerate(self.allFilesList):
                    filename = self.path2SaveEtl + self.pathFiles[i].split("/")[1]
                    file.to_csv(filename,index=False)
            else:
                raise ValueError("Falha ao salvar arquivos")
        else:
            filename = self.path2SaveEtl + self.pathFiles[index].split("/")[1]
            self.file.to_csv(filename,index=False)
               
    def makeEtl(self,index):
        #index = index
        self.readAllFiles(index)
        self.subNoneAsZero(index)
        #self.clearNullValues(self,index)
        self.ajustTypes(index)
        self.sumSameColuns(index)
        self.removeDuplicates(index)
        self.saveFiles(index)
        if(index == -1):
            self.returnAllFiles()
        else:
            self.returnFile()
        