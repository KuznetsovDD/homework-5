# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример:
# 2 4
# 2




def sum(a,b):
    if b==0:
        return a
    return a+sum(1,b-1)

def imputNumb():
    return int(input('Введите число: '))

a = imputNumb()
b = imputNumb()
print(sum(a,b))