"""3. Napisz programy wyznaczajace iloczyny stosujac petle for
d) odwrotnosci kwadratów w n-liczb.
"""
from math import modf


def multiplication(number,y):
    iloczyn=1
    for i in range(1,number+1):
        # print(pow(i,y))
        iloczyn *=pow(i,y)

    return 1/iloczyn

print(multiplication(3,2))
