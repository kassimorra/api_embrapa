from fastapi import FastAPI, Security, Response
from fastapi.responses import RedirectResponse
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer

from helpers.download import downloadFiles
from helpers.embrapaFiles import embrapaFiles

app = FastAPI()

@app.get('/', include_in_schema=False)
async def docs() -> RedirectResponse:
    return RedirectResponse(url='/docs')

#jwt
access_security = JwtAccessBearer(secret_key="secret_key", auto_error=True)

#jwt routes
@app.post("/auth")
def auth():
    subject = {"username": "username", "role": "user"}
    return {"access_token": access_security.create_access_token(subject=subject)}

@app.post("/auth_cookie")
def auth(response: Response):
    subject = {"username": "username", "role": "user"}
    access_token = access_security.create_access_token(subject=subject)
    access_security.set_access_cookie(response, access_token)
    return {"access_token": access_token}

@app.get("/users/me")
def read_current_user(
    credentials: JwtAuthorizationCredentials = Security(access_security),
):
    return {"username": credentials["username"], "role": credentials["role"]}


####

@app.get('/getFile/<index>')
def getProd(index, credentials: JwtAuthorizationCredentials = Security(access_security)):
        embFiles = embrapaFiles()
        fileName = embFiles.getFile(int(index))
        #download embrapa filename
        downloadFile = downloadFiles()
        return downloadFile.download(fileName)
    
@app.get('/getFile')
def getAll(credentials: JwtAuthorizationCredentials = Security(access_security)):
        embFiles = embrapaFiles()
        for i in range(len(embFiles.files)):
            fileName = embFiles.getFile(i)
            #download embrapa filename
            downloadFile = downloadFiles()
            downloadFile.download(fileName)
        return "end"

####