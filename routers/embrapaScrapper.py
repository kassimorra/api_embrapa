from fastapi import APIRouter, HTTPException, status, Depends
from webscrapper import Utils, Scrapper, BaseOptions
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
import json

router = APIRouter(
    prefix="/scrapper"
)

@router.get('/listAll', tags=["Web Scrapper Embrapa"])
async def list_all_embrapa_links_for_scrapping():
    instance_base_options = BaseOptions.EmbrapaBaseOptions()
    return JSONResponse(content=jsonable_encoder(list(instance_base_options.base_options.keys())), status_code = status.HTTP_200_OK)

@router.get('/download', tags=["Web Scrapper Embrapa"])
async def download_embrapa_with_webScrapping(file_name: str, ano: int = None):
    """

    Args:
    """
    base_scrapper: Utils.EmbrapaScrapperResponses = Utils.EmbrapaScrapperResponses(file_name, ano)
    if base_scrapper.verify_date() == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data não encontrada, entre uma data válida")

    try:        
        Scrapper.embrapa_save_data(base_scrapper)
    except:
        raise Exception
    
    return Response(content=json.dumps({"Response":"Sucess"}), media_type="application/json", status_code = 200)