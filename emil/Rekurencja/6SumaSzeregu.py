'''
6. Napisz rekurencyjna funkcje sumujaca pierwszych n składników szeregu
1 + 1/2 + 1/3 + 1/4 + ....
'''
def sumuj_szereg(n):
    if n == 1 :
        return 1
    elif n>1:
        return 1/n + sumuj_szereg(n-1)


print(sumuj_szereg(4))

