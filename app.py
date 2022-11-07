from flask import Flask, request, jsonify
from marshmallow.exceptions import ValidationError

from models import RequestParams
from builder import build_query

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.post("/perform_query")
def perform_query():
    try:
        query_params = RequestParams().load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    try:
        result = build_query(query_params)
    except FileNotFoundError as e:
        return jsonify(e.strerror), 400

    return jsonify(result), 200


if __name__ == '__main__':
    app.run()
