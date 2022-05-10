import os
import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps

import json

app = Flask(__name__)

@app.route('/retailer')
def retailer_data():
  print("=== Retailer  ==", flush=True)

  client = MongoClient(host='retailer_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["retailer_db"]

  retailer = db.retailer_tb.find({"name": "Retailer"})
  retailer = list(retailer)
  retailer = dumps(retailer)
  print(retailer, flush=True)
  return retailer

@app.route('/start_retailer_agent')
def start_retailer_agent():
  os.system('jupyter nbconvert --to notebook --inplace --execute retailer.ipynb')
  return "Retailer ran successfully"
