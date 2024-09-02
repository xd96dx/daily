import pandas as pd
from config import config


# 连跌策略, 根据POLICY_DAY 设置连跌的天数
def policy_down(file, stock_code: str, array: pd.Series):
    days = config.get_decrease()
    fall_five_day = (array[days:] < 0).all()
    if fall_five_day:
        tmp = f"down{-days}天: {stock_code} average: {array[days:].mean()}\n"
        file.write(tmp)
        file.flush()


# 连涨策略, 根据POLICY_DAY 设置连涨的天数
def policy_up(file, stock_code: str, array: pd.Series):
    days = config.get_increase()
    up_five_day = (array[days:] > 0).all()
    if up_five_day:
        tmp = f"up{-days}天: {stock_code}  average: {array[days:].mean()}\n"
        file.write(tmp)
        file.flush()


def policy_decline(file, stock_code: str, array: pd.Series):
    days = config.get_sum_day()
    sum_by_day = array[-days:].sum()
    if sum_by_day < -config.get_sum_by_day():
        tmp = f"{days}天 {stock_code} 跌幅: {sum_by_day}\n"
        file.write(tmp)
        file.flush()
