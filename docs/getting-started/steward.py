import os
import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps
from apscheduler.schedulers.background import BackgroundScheduler

import json

def policy_enforcer():
  print("Policy enforcer is running!")

sched = BackgroundScheduler()
sched.add_job(func=policy_enforcer, trigger='interval', seconds=1)
sched.start()

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

@app.route('/get_pool_config')
def send_pool_config():
  client = MongoClient(host='steward_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["steward_db"]
  print('========Point 1')
  pool = db.steward_tb.find_one({"name": "pool1"})
  pool = dumps(pool)
  print('========Point 2')
  print(pool)
  print('========Point 3')
  return pool

@app.route('/start_steward_agent')
def start_steward_agent():
  #os.system('jupyter nbconvert --to notebook --inplace --execute steward.ipynb')
  os.system('jupyter notebook steward.ipynb --ip=0.0.0.0')

  return "Steward ran successfully"

@app.route('/get_trust_anchor_verinym', methods = ['POST'])
def get_trust_anchor_verinym():
  entity = request.get_json( )
  entity = entity['entity']
  
  client = MongoClient(host='steward_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["steward_db"]

  print(entity)
  db.steward_tb.insert_one(entity);

  db.steward_tb.find_one_and_update({"name": "verinym_for"}, { "$set": { "value": entity["name"] } }, upsert=True);

  print(entity, flush=True)

  # os.system('jupyter nbconvert --to notebook --inplace --execute steward_get_verinym.ipynb')
  os.system('jupyter notebook steward_get_verinym.ipynb --ip=0.0.0.0')

  entity = db.steward_tb.find_one({"name": entity["name"]})

  print(entity, flush=True)

  return entity

if __name__ == "__main__":
  app.run()
