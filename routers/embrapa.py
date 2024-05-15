from fastapi import Depends, APIRouter, HTTPException, status
from helpers.embrapaFiles import embrapaFiles
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/embrapa"
)

@router.get('/listFiles', tags=["Download Embrapa"])
def lista_arquivos_da_embrapa():
    """
    Lista todos os arquivos da Embrapa com o seu respectivo ID
    """
    return JSONResponse(content=jsonable_encoder(embrapaFiles().listAll()), status_code = status.HTTP_201_CREATED)

@router.get('/getFile/<index>', tags=["Download Embrapa"])
def download_de_arquivo_unico(index: int):
    """
    Faz o download de um arquivo da Embrapa com base no seu id de referência (index)
    """
    try:
        embrapaFiles().embrapaDownloadFile(index)
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}
    
@router.get('/getFile', tags=["Download Embrapa"])
def download_de_todos_arquivos():
    """
    Faz o download de todos os arquivos da Embrapa
    """    
    try:
        embrapaFiles().embrapaDownloadAll()
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}