'''2. Napisz program, który wyznaczy sume cyfr liczby naturalnej.'''
def suma_naturalnej(n):
    if n==0:
        return 0
    elif n>0 and n<=9:
        return n
    elif n>9 and n<=99:
        return n//10 + suma_naturalnej(n%10)
    elif n>=100 and n<=999:
        return n//100 + suma_naturalnej(n%10)+ suma_naturalnej((n//10)%10)

print(suma_naturalnej(125))






