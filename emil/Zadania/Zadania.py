# Task1
"""Let's say you have a 32-bit long integer - call it N .
You have to return it with its digits in
reversed form. If the modified value will go over the 32-bit integer range (signed), return 0"""

from collections import defaultdict


def bit(number):
    min = -2147483648
    max = 2147483647
    if int(number) >= min and int(number) < 0:
        return '{}{}'.format('-',number[:-len(number):-1])
    elif int(number) > 0 and int(number) <= max:
        return '{}'.format(number[::-1])
    else:
        return 0


print(bit("512000000"))

#Task2
"""Alright, here's the second task. Let's say you have a phone dial, like in the picture below.
You have to generate all the possible letter combinations for phone numbers that the user
might want to check. There are some examples below; you'll get it!
"""

def digit():
    global sign
    global dict
    sign = ["","","",'a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    dict = defaultdict(int)
    for i in range(0,9):
        if i in (0,1,2,3,4,5):
            dict[i+1] = sign[3*i:3*i+3]

            if i == 0:
                dict[0] = '+'
            # lista.append(sign[3*i:3*i+3])
        elif i == 6:
            dict[i+1] = sign[3*i:3*i+4]
            # lista.append(sign[3*i:3*i+4])
        elif i == 7:
            dict[i+1] = sign[3*i+1:3*i+4]
            # lista.append(sign[3*i+1:3*i+4])
        elif i == 8:
            dict[i+1] = sign[3*i+1:3*i+5]
            # lista.append(sign[3*i+1:3*i+5])
    return dict



def convert_to_list(text):
    digit()

    global word

    word = []
    for i in text:
        if int(i) in dict.keys():
            word.append(dict[int(i)])
    return word

convert_to_list("45")


"""NIESKONCZONE
"""



# print(dial('45'))
