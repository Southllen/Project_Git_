import random

def generateList(a, b, n):
    l=list(range(n))
    i = 0
    while i < n:
        l[i] = random.randint(a, b)
        i = i + 1
    print(l)

generateList(0, 9, 10)
