from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/cadastro', methods = ['POST', 'GET'])
@cross_origin()
def hello_world():
    print(request.json)
    return {
        "message": "usuario cadastrado com sucesso!"
    }

@app.route('/roberta-linda', methods = ['GET'])
@cross_origin()
def roberta():
    return {
        "message": "ROBERTA EU TE AMO"
    }