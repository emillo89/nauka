'''7. Napisz rekurencyjna funkcje sumujaca pierwszych n składników szeregu
1 + 1/2 - 1/3 + 1/4 - 1/5'''


def suma_szeregu(n):
    if n == 1:
        return 1
    elif n > 1:
        return 1/n * ((-1)**n) + suma_szeregu(n-1)


print(suma_szeregu(4))
