import os

from flask import Flask, request, jsonify
from marshmallow.exceptions import ValidationError

from models import RequestParams
from builder import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    try:
        query_params = RequestParams().load(request.args)
    except ValidationError as e:
        return jsonify(e.messages), 400

    try:
        result = build_query(query_params)
    except FileNotFoundError as e:
        return jsonify(e.strerror), 400

    return jsonify(result), 200


if __name__ == '__main__':
    app.run()
