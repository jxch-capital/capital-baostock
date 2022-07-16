from flask import Flask
from grafana.json_api import json_api
from grafana.baostock_api import baostock_api

app = Flask(__name__)
app.register_blueprint(json_api)
app.register_blueprint(baostock_api)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True)
