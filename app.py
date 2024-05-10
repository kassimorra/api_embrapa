from flask import Flask, request
import pandas as pd
from helpers import download, embrapaFiles

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
        
@app.route('/getFile/<index>', methods=['GET'])
def getProd(index):
    #get Filename from Index
    embFiles = embrapaFiles.embrapaFiles()
    fileName = embFiles.getFile(int(index))
    #download embrapa filename
    downloadFile = download.downloadFiles()
    return downloadFile.download(fileName)

@app.route('/getFile', methods=['GET'])
def getAll():
    #get Filename from Index
    embFiles = embrapaFiles.embrapaFiles()
    for i in range(len(embFiles.files)):
        fileName = embFiles.getFile(i)
        #download embrapa filename
        downloadFile = download.downloadFiles()
        downloadFile.download(fileName)
    return "end"
