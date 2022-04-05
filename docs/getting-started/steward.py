import os
import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps

import json

app = Flask(__name__)

@app.route('/steward')
def steward_data():
  print("=== Steward  ==", flush=True)

  client = MongoClient(host='steward_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["steward_db"]

  steward = db.steward_tb.find({"name": "Sovrin Steward"})
  steward = list(steward)
  steward = dumps(steward)
  print(steward, flush=True)
  return steward

@app.route('/start_steward_agent')
def start_steward_agent():
  os.system('jupyter nbconvert --to notebook --inplace --execute steward.ipynb')
  return "Steward ran successfully"

@app.route('/get_verinym')
def get_verinym():
  os.system('jupyter nbconvert --to notebook --inplace --execute steward_get_verinym.ipynb')
  return "Steward ran successfully"
