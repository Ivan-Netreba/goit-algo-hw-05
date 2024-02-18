from typing import Callable
from functools import reduce
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, повнений додатковими надходженнями 27.45 і 324.00 доларів ."\
"1000000.00 просто рандомні числа для перевірки патерна. Код їх вже не враховує! 1000000.00"

def generator_numbers(text: str):
    numbers = map(float, re.findall(r"\ \d+\.{0,1}\d+.\ ", text))
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):   
    total_income = reduce(lambda x,y: x+y, func(text))
    return f"Загальний дохід: {total_income}"

total_income = sum_profit(text, generator_numbers)
print(total_income)
