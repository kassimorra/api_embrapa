from fastapi import Depends, APIRouter, HTTPException, status
from helpers.etlFiles import etlFiles

router = APIRouter(
    prefix="/etl"
)

@router.get('/getFile/<index>', tags=["Download Embrapa and Make ETL in Files"])
def Get_Single_File(index: int):
    try:
        etlFiles.makeEtl(index)
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}
    
@router.get('/getFile', tags=["Download Embrapa and Make ETL in Files"])
def Get_All_Files():
    try:
        etlFiles.makeEtl(-1)
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}