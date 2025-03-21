import re as r

def generator_numbers(text):
    numbers = r.findall(r"\b\d+\.\d+\b", text)
    for number in numbers:
        yield float(number)

def sum_profit(text, generator_numbers):
    total_profit = 0
    for number in generator_numbers(text):
        total_profit += number
    return total_profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
