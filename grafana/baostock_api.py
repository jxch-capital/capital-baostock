from flask import Blueprint, request
import stock.bs_utils as bsu
import baostock as bs

baostock_api = Blueprint('baostock_api', __name__)


@baostock_api.route("/grafana/", methods=["get"])
def root():
    return '{"status":"success"}'


@baostock_api.route("/grafana/daily_stock_names", methods=["POST"])
def daily_stock_names():
    names = request.json.get('names')
    start = request.json.get('start')
    end = request.json.get('end')
    print("----> /grafana/daily_stock_names", names, start, end)
    bs.login()
    json_arr = bsu.query_daily_k_json_by_names(names, bsu.time_to_str(start), bsu.time_to_str(end))
    bs.logout()
    print("<---- /grafana/daily_stock_names", names, start, end)
    return json_arr


@baostock_api.route("/grafana/daily_stock_codes", methods=["POST"])
def daily_stock_codes():
    codes = request.json.get('codes')
    start = request.json.get('start')
    end = request.json.get('end')
    print("----> /grafana/daily_stock_codes", codes, start, end)
    bs.login()
    json_arr = bsu.query_daily_k_json(codes, bsu.time_to_str(start), bsu.time_to_str(end))
    bs.logout()
    print("<---- /grafana/daily_stock_codes", codes, start, end)
    return json_arr
