from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
        
@app.route('/getComercio', methods=['GET'])
def getComercio():
    arch = pd.read_csv("arquivos/Comercio.csv", sep = ";")
    arch.to
    return arch.to_json()

@app.route('/getExp', methods=['GET'])
def getExp():
    arquivo = request.args.get('arquivo')
    arch = pd.read_csv("arquivos/Exp" + arquivo + ".csv", sep = ";")
    return arch.to_json()

@app.route('/getImp', methods=['GET'])
def getImp():
    arquivo = request.args.get('arquivo')
    arch = pd.read_csv("arquivos/Imp" + arquivo + ".csv", sep = ";")
    return arch.to_json()

@app.route('/getProcessamento', methods=['GET'])
def getProcessamento():
    arquivo = request.args.get('arquivo')
    arch = pd.read_csv("arquivos/Processa" + arquivo + ".csv", sep = ";")
    return arch.to_json()