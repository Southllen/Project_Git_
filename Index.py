import random


def generatelist(a, b, n):
    l = list(range(n))
    i = 0
    while i < n:
        l[i] = random.randint(a, b)
        i = i + 1
    return l


element = generatelist(0, 30, 12)
print(element)
n = int(input('Введите число от 0 до 12:'))
element[n]= n
print(element)