money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 1  # количество месяцев, которое можно прожить

while money_capital + (salary - spend) >= spend:
    money_capital += salary - spend
    spend = spend * (1+ increase)

    month += 1
print(month)
