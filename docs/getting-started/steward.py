import asyncio
import time
import logging
import sys
from threading import Thread
import pymongo
from pymongo import MongoClient
from indy import anoncreds, did, ledger, pool, wallet, IndyError
from flask import Flask, request, jsonify

import json

# async def run():
#   print("Steward -> started")

#   # Set protocol version 2 to work with Indy Node 1.4
#   await pool.set_protocol_version(2)

#   pool_ = {
#       'name': 'pool1',
#       'config': json.dumps({"genesis_txn": '/home/indy/sandbox/pool_transactions_genesis'})
#   }
#   print("Open Pool Ledger: {}".format(pool_['name']))

#   try:
#       await pool.create_pool_ledger_config(pool_['name'], pool_['config'])
#   except IndyError as ex:
#       if ex.error_code == ErrorCode.PoolLedgerConfigAlreadyExistsError:
#           pass
#   pool_['handle'] = await pool.open_pool_ledger(pool_['name'], None)

#   print("==============================")
#   print("=== Creating Steward  ==")
#   print("------------------------------")

#   steward = {
#       'name': "Sovrin Steward",
#       'wallet_config': json.dumps({'id': 'sovrin_steward_wallet'}),
#       'wallet_credentials': json.dumps({'key': 'steward_wallet_key'}),
#       'pool': pool_['handle'],
#       'seed': '000000000000000000000000Steward1'
#   }

#   await create_wallet(steward)

#   print("\"Sovrin Steward\" -> Create and store in Wallet DID from seed")
#   steward['did_info'] = json.dumps({'seed': steward['seed']})
#   steward['did'], steward['key'] = await did.create_and_store_my_did(steward['wallet'], steward['did_info'])

#   print("==============================")

#   print(" \"Sovrin Steward\" -> Close and Delete wallet")
#   await wallet.close_wallet(steward['wallet'])
#   await wallet.delete_wallet(steward['wallet_config'], steward['wallet_credentials'])

#   print("Close and Delete pool")
#   await pool.close_pool_ledger(pool_['handle'])
#   await pool.delete_pool_ledger_config(pool_['name'])

#   print("Getting started -> done")

# async def create_wallet(identity):
  # print("\"{}\" -> Create wallet".format(identity['name']))
  # try:
  #     await wallet.create_wallet(identity['wallet_config'], identity['wallet_credentials'])
  # except IndyError as ex:
  #     if ex.error_code == ErrorCode.PoolLedgerConfigAlreadyExistsError:
  #         pass
  # identity['wallet'] = await wallet.open_wallet(identity['wallet_config'], identity['wallet_credentials'])

# thread = Thread(target = run)
# thread.start()
# time.sleep(1)

app = Flask(__name__)

@app.route('/steward')
def steward_data():
  print("=== Vikram  ==", flush=True)

  client = MongoClient(host='steward_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["steward_db"]

  _animals = db.steward_tb.find()
  animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
  print(animals, flush=True)
  return jsonify({"animals": animals})

# thread.join()

# if __name__ == '__main__':
#   loop = asyncio.new_event_loop()
#   asyncio.set_event_loop(loop)
#   await run()
#   time.sleep(1)  # FIXME waiting for libindy thread complete
