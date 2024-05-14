from fastapi import Depends, APIRouter, HTTPException, status
from helpers.embrapaFiles import embrapaFiles

router = APIRouter(
    prefix="/embrapa"
)

@router.get('/getFile/<index>', tags=["Download Embrapa"])
def Get_Single_File(index: int):
    try:
        embrapaFiles().embrapaDownloadFile(index)
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}
    
@router.get('/getFile', tags=["Download Embrapa"])
def Get_All_Files():
    try:
        embrapaFiles().embrapaDownloadAll()
    except:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Failed to download file")
    return {"message": "sucesso"}