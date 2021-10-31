import random


def generatelist(a, b, n):
    l = list(range(n))
    i = 0
    while i < n:
        l[i] = random.randint(a, b)
        i = i + 1
    return l


element = generatelist(0, 9, 10)
print(element)
a = int(input('Введите число от 0 до 10:'))
element[a] = element.index(a)
print('Ваше число находится в списке под номером', element.index(a))