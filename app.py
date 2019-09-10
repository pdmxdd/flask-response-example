from flask import Flask, make_response
import json

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def get_index():
    return "index"

@app.route("/json", methods=["GET"])
def get_json():
    body_dict = {"body": "payload"}
    response = make_response(json.dumps(body_dict), 200)
    response.headers.add('Content-Type', 'application/json')
    return response

if __name__ == "__main__":
    app.run(port=8080)
