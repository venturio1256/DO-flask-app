#### Test Digital Ocean App deployment ###
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    id = request.args.get('id')
    username = request.args.get('name')
    #return jsonify({'IDealIST ': id, 'Name' : username})
    return jsonify(request.args)
    
