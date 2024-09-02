import baostock as bs
import pandas as pd
from config import TIME_LATE, TIME_NOW, TIME_EARLY, POLICY_DAY
from policys import policy_down, policy_up, policy_decline


def get_data(stock_code, need_print=False):
    rs = bs.query_history_k_data_plus(stock_code,
                                      "date,code,open,high,low,close,preclose,volume,"
                                      "amount,adjustflag,turn,tradestatus,pctChg,isST",
                                      start_date=TIME_EARLY, end_date=TIME_LATE,
                                      frequency="d", adjustflag="3")

    if rs.error_code != "0":
        print('query_history_k_data_plus respond error_code:'+rs.error_code)
        print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    data_list = []
    daily_list = []

    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        d = rs.get_row_data()
        data_list.append(d)
        try:
            daily_list.append(float(d[-2]))
        except BaseException:
            # print("err: ", stock_code, d)
            continue

    result = pd.DataFrame(data_list, columns=rs.fields)
    if need_print:
        print(result)

    file = open(TIME_NOW, "a")
    calculate(file, stock_code, pd.Series(daily_list))
    file.close()


def calculate(file, stock_code: str, array: pd.Series):
    policy_down(file, stock_code, array)
    policy_up(file, stock_code, array)
    policy_decline(file, stock_code, array)
    # add new policy here
    ...


def get_large_a():
    lg = bs.login()
    if lg.error_code != "0":
        print(lg.error_msg)
        print(lg.error_code)

    with open("HA", "r") as f:
        line = f.readline()
        while line:
            get_data("sh."+f.readline().strip())
            line = f.readline()

    with open("SA", "r") as f:
        line = f.readline()
        while line:
            get_data("sz."+f.readline().strip())
            line = f.readline()

    bs.logout()


if __name__ == '__main__':
    get_large_a()

    # lg = bs.login()
    # get_data("sh.688789", True)
    # bs.logout()

