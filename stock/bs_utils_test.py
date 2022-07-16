import bs_utils
import baostock as bs
import jsonpath
import json
import stock.bs_utils as bsu

bs.login()

# res_arr = bs_utils.query_daily_k_json(["sh.600000","sz.002739"], '2022-07-01')
#
# print(res_arr)
#
# u_str = json.loads(res_arr)
# ret = jsonpath.jsonpath(u_str, '$.浦发银行[*].close')
# print(ret)

res = bs_utils.query_codes_by_names(["中证100指数","中证200指数","中证500指数","中证800指数","中证1000指数"])
print(res)

# res = bs_utils.query_daily_k_json_by_names(["中证500指数","中证白酒指数","中证能源指数","中证新能源指数","中证医药卫生指数","中证主要消费指数","中证可选消费指数","中证信息技术指数","中证大宗商品股票指数","中证500工业指数","中证金融地产指数","中证互联网金融指数","中证军工指数"], '2022-07-01')
# print(res)

rs = bs_utils.query_daily_k_json_by_names(["中证100指数","中证200指数","中证500指数","中证800指数","中证1000指数"], '2022-07-01')
print(rs)
# rs = bs.query_stock_basic(code_name='中证')
# df = bsu.rs_to_dataframe(rs)
# df.to_csv(r"E:\work\jxch-capital\capital-baostock\out\中证.csv", index=False)
# print(df)

bs.logout()