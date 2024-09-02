from datetime import datetime, timedelta

DAYS = 15  # total days
POLICY_DAY = -5  # default policy day
INCREASE_DAY = 0  # 连涨天数
DECREASE_DAY = 0  # 连跌天数
SUM_DAY = 3  # 计算多少日的总跌幅
SUM_BY_DAY = 10  # 几日内的跌幅

TIME_NOW = datetime.now().strftime("%Y-%m-%d")
TIME_LATE = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
TIME_EARLY = (datetime.now() - timedelta(days=DAYS)).strftime("%Y-%m-%d")


class Config:

    def __init__(self):
        if DECREASE_DAY != 0:
            self.decrease_day = DECREASE_DAY
        else:
            self.decrease_day = POLICY_DAY

        if INCREASE_DAY != 0:
            self.increase_day = INCREASE_DAY
        else:
            self.increase_day = POLICY_DAY

        self.sum_day = SUM_DAY
        self.sum_by_day = SUM_BY_DAY

    def get_increase(self):
        return self.increase_day

    def get_decrease(self):
        return self.decrease_day

    def get_sum_day(self):
        return self.sum_day

    def get_sum_by_day(self):
        return self.sum_by_day


config = Config()

