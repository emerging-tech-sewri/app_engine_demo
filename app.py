"""
1. get request (VIN, to, from date, category)
2. check with Bigquery if VIN exists for that date range
3. if yes send file_array to function data_handler
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/test')
def test():
    return "App engine is reachable"


if __name__ == "__main__":
    app.run(port=8080, host="localhost")