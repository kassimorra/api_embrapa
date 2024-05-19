from fastapi import APIRouter, HTTPException, status
from helpers.hlpEmbrapa import get_index_filename, embrapa_download
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/embrapa"
)

@router.get('/listFiles', tags=["Download Embrapa"])
def lista_arquivos_da_embrapa():
    """
    Lista todos os arquivos da Embrapa com o seu respectivo ID. Ids usados no download na rota /getFile
    """
    return JSONResponse(content=jsonable_encoder(get_index_filename()), status_code = status.HTTP_201_CREATED)

@router.get('/getFile', tags=["Download Embrapa"])
def download_de_arquivo(index: int | None = None):
    """
    Faz o download de um arquivo da Embrapa com base no seu id de referência (index) ou o download de todos arquivos caso o parametro index não seja informado.
    
    Args:
        index (int) Opcional: índice do arquivo a ser feito o download. Pode ser obtido pela rota /listFiles
    """
    try:
        embrapa_download(index)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}