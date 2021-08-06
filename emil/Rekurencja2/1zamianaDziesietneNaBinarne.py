'''1. Napisz program, który zapisze podana liczbe dziesietna naturalna w systemie
binarnym.'''

import math
def dziesietne_to_bin(dzie):
    '''zzmiana dziesietne na binarne za pomoca rekurencji ale nalezy czytac od konca, jak to poprawic?'''
    if dzie == 0 :
        return ""
    elif dzie>0:
        return str(dziesietne_to_bin(dzie // 2)) + str(dzie % 2)

        # return str(dzie%2) + str(dziesietne_to_bin(dzie//2))

print(dziesietne_to_bin(55))


def bin_dziesietne(bin):
    if len(str(bin)) == 0:
        return 0
    elif len(str(bin))> 0:
        return (pow(2,len(str(bin))-1) * int(bin[0]))+ int(str(bin_dziesietne(bin[1:])))
print(bin_dziesietne('110111'))

print('---------------------------------------------------------------')
print(1%2)

# binarne move to dziesietne
# def bin_to_dziesietne(bin):
#     dziesietna = 0
#     suma = 0
#     for i in reversed(range(len(bin))):
#         if bin[i] == '1':
#             dziesietna = pow(2,abs(i-(len(bin)-1)))
#             suma +=dziesietna
#
#     return 'suma= ',suma
#
# print(bin_to_dziesietne('0110111'))



# def reversedd(bin):
#     ''' Funkcja przykładowa, sprawdzajaca odwrócone indexy'''
#     for i in reversed(range(len(bin))):
#         print(abs(i-(len(bin)-1)),' ', bin[i])
#
#
# reversedd('10011')



