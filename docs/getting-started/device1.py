import os
import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps

import json

app = Flask(__name__)

@app.route('/device1')
def device1_data():
  print("=== device1  ==", flush=True)

  client = MongoClient(host='device1_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["device1_db"]

  device1 = db.device1_tb.find({"name": "device1"})
  device1 = list(device1)
  device1 = dumps(device1)
  print(device1, flush=True)
  return device1

@app.route('/start_device1_agent')
def start_supplier_agent():
  os.system('jupyter nbconvert --to notebook --inplace --execute device1.ipynb')
  return "Started Device1 successfully"

@app.route('/accept_credential_offer_request', methods = ['POST'])
def accept_credential_offer_request():
  offer = request.get_json()
  #offer = entity['offer']
  client = MongoClient(host='device1_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["device1_db"]
 
  db.device1_db.insert_one({offer});
  db.steward_tb.find_one_and_update({"name": "credential_offer"}, { "$set": { "value": offer} }, upsert=True);

  return "Credential offer accepted successfully"


@app.route('/request_credential_from_supplier', methods = ['GET'])
def send_cred_request_to_supplier():

