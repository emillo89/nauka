"""3. Napisz programy wyznaczajace iloczyny stosujac petle for
a) iloczyn kolejnych liczb
"""

def multiplication(number):
    iloczyn=1
    for i in range(1, number+1):
        iloczyn = iloczyn*i
    return iloczyn

print(multiplication(3))