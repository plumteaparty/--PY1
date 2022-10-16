money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while money_capital >= spend:
    month += 1
    debt = salary-spend
    money_capital = money_capital+debt
    spend = spend * (1 + increase)

print(month)
