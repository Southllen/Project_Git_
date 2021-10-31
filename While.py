def name(a, b, c):
    while a < b:
        print(a + c)
        a = a + c
    else:
        print("bingo!")

name(0, 20, 2)
