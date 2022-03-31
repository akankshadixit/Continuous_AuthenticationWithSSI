db = db.getSiblingDB("steward_db");
db.steward_tb.drop();


db.steward_tb.insertMany([
  {
      "id": 1,
      "name": "Lion",
      "type": "wild"
  }
]);