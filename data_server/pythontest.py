#import pandas as pd
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test')
def index():
    # return json.dumps('Hello World!')
    user = {"user": {"name": "Shankhanil", "dept": "MCA"}}
    return json.dumps(user)
    # return """
    # <h1>Python Flask in a Docker</h1>
    # """

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)