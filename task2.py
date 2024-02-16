from typing import Callable
from functools import reduce
import re

text = "Загальний дохід працівника складається з декількох частин:"\
    "1000.01 як основний дохід, повнений додатковими надходженнями"\
    "27.45 і 324.00 доларів."

def generator_numbers(text: str):
    pattern = r"\d+.\d+"
    list_str = re.findall(pattern,text)
    list_float = ([float(i) for i in list_str])
    yield list_float

def sum_profit(text: str, func: Callable):
    a = generator_numbers(text) 
    income = (next(a))
    total_income = reduce(lambda x,y: x+y, income)
    print(f"Загальний дохід: {total_income}")

total_income = sum_profit(text, generator_numbers)