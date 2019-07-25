import psycopg2, pandas as pd
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test')
def index():
    # return json.dumps('Hello World!')
    user = {"user": {"name": "Shankhanil", "dept": "MCA"}}
    return json.dumps(user)

if __name__ == "__main__":
    print("server is running on localhost!!")
    app.run(host="localhost", port=6000, debug=True)