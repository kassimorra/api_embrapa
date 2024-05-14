from fastapi import Depends
from fastapi.responses import RedirectResponse
from helpers.fastapiconf import initFast
import authentication as auth
from routers.authentication import router as auth_route
from routers.embrapa import router as embrapa_route

app = initFast()

app.include_router(auth_route)
app.include_router(embrapa_route, dependencies=[Depends(auth.oauth2_scheme)])

@app.get('/', include_in_schema=False)
async def docs() -> RedirectResponse:
    return RedirectResponse(url='/docs')