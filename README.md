# policy

## install
```shell
    pip install baostock -i https://pypi.org/simple 
```


## policy
```python
#policys.py 中新增策略, 添加在calculate() 方法中
def calculate(file, stock_code: str, array: pd.Series):
    policy_down(file, stock_code, array)
    policy_up(file, stock_code, array)

    # add new policy here
    ...

DAYS: 总区间
POLICY_DAY: 默认连续涨跌天数(负数)
INCREASE_DAY: 连涨天数(负数)
DECREASE_DAY: 连跌天数(负数)
```


## run
```shell
    python3.10 main.py
```