"""3. Napisz programy wyznaczajace iloczyny stosujac petle for
c) iloczyn kolejnych liczb 1/(k(k+1))
"""

def multiplication(number):
    iloczyn=1
    for i in range(1, number+1):
        iloczyn = iloczyn*(1/(i*(i+1)))
    return iloczyn

print(multiplication(3))