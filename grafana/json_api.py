from flask import Blueprint, request
import baostock as bs
import time
import stock.bs_utils as bsu

json_api = Blueprint('json_api', __name__)


@json_api.route("/grafana/json/test", methods=["get"])
def test():
    return "test json api"


@json_api.route("/grafana/json/", methods=["get"])
def root():
    return '{"status":"success"}'



@json_api.route("/grafana/json/query", methods=["post"])
def query():
    codes = request.json.get('code')
    start = time.localtime(request.json.get('start'))
    end = time.localtime(request.json.get('end'))
    start = time.strftime("%Y-%m-%d", start)
    end = time.strftime("%Y-%m-%d", end)
    bs.login()
    json_arr = bsu.query_daily_k_json(codes, start, end)
    bs.logout()
    return json_arr


@json_api.route("/grafana/json/search", methods=["post"])
def search():
    return '["search_test"]'


@json_api.route("/grafana/json/annotations", methods=["post"])
def annotations():
    return '{"annotations_test":"success"}'
