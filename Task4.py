#Задание 4
print("Введите выручку фирмы: ")
earnings = int(input())

print("Введите издержки фирмы: ")
cost = int(input())
result = earnings - cost

if (cost > 0):
    print(f"Финансовый результат - прибыль. Её величина: {result}")
else:
    print(f"Финансовый результат - убыток. Её величина: {result}")

profitability = result / earnings
print(f"Рентабельность выручки = {profitability}")

print("Введите численность сотрудников фирмы: ")
strength = int(input())
company_profit = result / strength
print(f"Прибыль фирмы в расчете на одного сотрудника = {company_profit}")