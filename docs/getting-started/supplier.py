import os
import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps

import json

app = Flask(__name__)

@app.route('/supplier')
def supplier_data():
  print("=== Supplier  ==", flush=True)

  client = MongoClient(host='supplier_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["supplier_db"]

  supplier = db.supplier_tb.find({"name": "Supplier"})
  supplier = list(supplier)
  supplier = dumps(supplier)
  print(supplier, flush=True)
  return supplier

@app.route('/start_supplier_agent')
def start_supplier_agent():
  os.system('jupyter nbconvert --to notebook --inplace --execute supplier.ipynb')
  return "Supplier ran successfully"

@app.route('/generate_crdential_schema')
def generate_credential_schema():
  os.system('jupyter notebook supplier_generate_credential_schema.ipynb --ip=0.0.0.0')

@app.route('/send_credential_offer_to_device', methods = ['POST'])
def send_credential_offer_to_device():
  entity = request.get_json( )
  entity = entity['entity']

  client = MongoClient(host='supplier_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["supplier_db"]

  db.steward_tb.find_one_and_update({"name": "send_credential_offer_to_device"}, { "$set": { "value": entity } }, upsert=True);

  print(entity, flush=True)

  os.system('jupyter notebook send_credential_offer_to_device.ipynb --ip=0.0.0.0')