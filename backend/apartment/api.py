import json
from flask import Flask, jsonify, request
from apartment.tasks import search_leboncoin
from .addons import cors, anounces_db

app = Flask(__name__)
cors.init_app(app)


@app.route("/anounces/search")
def search_anounces():
    task = search_leboncoin.delay()
    return jsonify({"task_id": str(task)})


@app.route("/anounces")
def list_anounces():
    anounces = anounces_db.search()
    return jsonify(anounces)


@app.route("/anounces/inbox/<string:anounce_id>", methods=["POST"])
def set_anounce_as_inbox(anounce_id):
    anounces_db.set_decision(anounce_id, "inbox")
    return "updated successfully"


@app.route("/anounces/favorites/<string:anounce_id>", methods=["POST"])
def set_anounce_as_favorite(anounce_id):
    anounces_db.set_decision(anounce_id, "favorite")
    return "updated successfully"


@app.route("/anounces/blacklist/<string:anounce_id>", methods=["POST"])
def set_anounce_as_blacklisted(anounce_id):
    anounces_db.set_decision(anounce_id, "blacklist")
    return "updated successfully"
