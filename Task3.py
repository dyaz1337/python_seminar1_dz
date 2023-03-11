#Задание 3
print("Введите целое положительное число: ")
num = int(input())
if (num < 0):
    print("Это не положительное число. Попробуйте еще раз :)")
else:
    sum = num + num * 11 + num * 111
    print(f"{num} + {num * 11} + {num * 111} = {sum}")
