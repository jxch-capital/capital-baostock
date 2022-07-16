from flask import Blueprint, request
import stock.bs_utils as bsu
import baostock as bs
import logging
logging.basicConfig(level = logging.INFO)

baostock_api = Blueprint('baostock_api', __name__)


@baostock_api.route("/grafana/", methods=["get"])
def root():
    return '{"status":"success"}'


@baostock_api.route("/grafana/daily_stock_names", methods=["POST"])
def daily_stock_names():
    names = request.json.get('names')
    start = request.json.get('start')
    end = request.json.get('end')
    logging.info(f"----> /grafana/daily_stock_names, args: names={names}, start={start}, end={end}")
    bs.login()
    json_arr = bsu.query_daily_k_json_by_names(names, bsu.time_to_str(start), bsu.time_to_str(end))
    bs.logout()
    logging.info(f"<---- /grafana/daily_stock_names, args: names={names}, start={start}, end={end}")
    return json_arr


@baostock_api.route("/grafana/daily_stock_codes", methods=["POST"])
def daily_stock_codes():
    codes = request.json.get('codes')
    start = request.json.get('start')
    end = request.json.get('end')
    logging.info(f"----> /grafana/daily_stock_codes, args: names={codes}, start={start}, end={end}")
    bs.login()
    json_arr = bsu.query_daily_k_json(codes, bsu.time_to_str(start), bsu.time_to_str(end))
    bs.logout()
    logging.info(f"<---- /grafana/daily_stock_codes, args: names={codes}, start={start}, end={end}")
    return json_arr
