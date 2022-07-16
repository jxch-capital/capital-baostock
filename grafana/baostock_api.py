from flask import Blueprint, request
import baostock as bs
import stock.bs_utils as bsu
import grafana.support as support

baostock_api = Blueprint('baostock_api', __name__)


@baostock_api.route("/grafana/", methods=["get"])
def root():
    return '{"status":"success"}'


@support.cache_with_param()
@baostock_api.route("/grafana/daily_stock_names", methods=["POST"])
def daily_stock_names():
    names = request.json.get('names')
    start = request.json.get('start')
    end = request.json.get('end')
    print("----> /grafana/daily_stock_names", names, start, end)
    bs.login()
    json_arr = bsu.query_daily_k_json_by_names(names, bsu.time_to_str(start), bsu.time_to_str(end))
    bs.logout()
    print("<---- /grafana/daily_stock_names", names, start, end, json_arr)
    return json_arr


@support.cache_with_param()
@baostock_api.route("/grafana/daily_stock_codes", methods=["POST"])
def daily_stock_codes():
    codes = request.json.get('codes')
    start = request.json.get('start')
    end = request.json.get('end')
    print("----> /grafana/daily_stock_codes", codes, start, end)
    bs.login()
    json_arr = bsu.query_daily_k_json(codes, bsu.time_to_str(start), bsu.time_to_str(end))
    bs.logout()
    print("<---- /grafana/daily_stock_codes", codes, start, end, json_arr)
    return json_arr
