"""3. Napisz programy wyznaczajace iloczyny stosujac petle for
b) iloczyn kolejnych liczb (2k-1)
"""

def multiplication(number):
    iloczyn=1
    for i in range(1, number+1):
        iloczyn = iloczyn*(2*i-1)
    return iloczyn

print(multiplication(3))