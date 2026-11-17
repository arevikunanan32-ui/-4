# Программа считает сумму чисел от 1 до N
n = int(input("Введите число: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Сумма:", total)
print("Среднее:", total / n)
