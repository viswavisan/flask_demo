from flask import Flask, jsonify,g

import time
app = Flask(__name__)
@app.route("/sync")
def sync_endpoint():
    time.sleep(3)
    return {"method": "sync"}