from fastapi import Depends, APIRouter
from helpers.download import downloadFiles
from helpers.embrapaFiles import embrapaFiles
import authentication as auth

router = APIRouter(
    prefix="/embrapa"
)

@router.get('/getFile/<index>')
def getFile(index):
        embFiles = embrapaFiles()
        fileName = embFiles.getFile(int(index))
        #download embrapa filename
        downloadFile = downloadFiles()
        return downloadFile.download(fileName)
    
@router.get('/getFile')
def getAll():
        embFiles = embrapaFiles()
        for i in range(len(embFiles.files)):
            fileName = embFiles.getFile(i)
            #download embrapa filename
            downloadFile = downloadFiles()
            downloadFile.download(fileName)
        return "end"