from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request

import pandas as pd
from helpers import download, embrapaFiles, configSwagger

users = {
    'example': {
        'password': 'password',
        'roles': ['user']
    }
}


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'qualquerStringAqui'  # Change this to a secure random key in production
jwt = JWTManager(app)

app.register_blueprint(configSwagger.swagger_ui_blueprint, url_prefix=configSwagger.SWAGGER_URL)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
       
@app.route('/getFile/<index>', methods=['GET'])
@jwt_required()
def getProd(index):
    try:
        verify_jwt_in_request()
        #get Filename from Index
        embFiles = embrapaFiles.embrapaFiles()
        fileName = embFiles.getFile(int(index))
        #download embrapa filename
        downloadFile = download.downloadFiles()
        return downloadFile.download(fileName)
    except Exception as e:
        return jsonify({"msg": str(e)}), 401
    
    

@app.route('/getFile', methods=['GET'])
@jwt_required()
def getAll():
    try:
        verify_jwt_in_request()
        embFiles = embrapaFiles.embrapaFiles()
        for i in range(len(embFiles.files)):
            fileName = embFiles.getFile(i)
            #download embrapa filename
            downloadFile = download.downloadFiles()
            downloadFile.download(fileName)
        return "end"
    except Exception as e:
        return jsonify({"msg": str(e)}), 401

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    user = users.get(username)
    if user and password == user['password']:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user = users.get(current_user)
    return jsonify(logged_in_as=current_user, email=user['email'], roles=user['roles']), 200

@app.route('/validate_token', methods=['GET'])
def validate_token():
    try:
        verify_jwt_in_request()
        return jsonify({"msg": "Token is valid"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 401
    
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users:
        return jsonify({"msg": "Username already exists"}), 400

    users[username] = {
        'password': password,
        'roles': ['user']
    }
    return jsonify({"msg": "User created successfully"}), 201
