"""
6.Napisz program rozwiazujacy zadania - zastosuj petle for i while czy
kazda z nich daje dobre rozwiazanie?
a) Kupiec podczas swojej podrózy handlowej do Wenecji podwoił
tam swój poczatkowy kapitał, a nastepnie wydał 12 denarów. Potem
udał sie do Florencji, gdzie znowu podwoił liczbe posiadanych
denarów i wydał 12 i ... został bez grosza. Ile denarów miał na poczatku?

"""
# za pomoca petli for:
import random

for i in range(1,100):
    if 2*(2*i -12) - 12 == 0:
        print('kupiec na poczatku mial: ',i, ' denarow')
# za pomoca petli while:
i = 0
while i<100:
    if 2*(2*i -12) - 12 == 0:
        print('kupiec na poczatku mial: ',i, ' denarow')
    i=i+1

"""
b)Kupiec podczas swojej podrózy handlowej do Wenecji podwoił tam swój poczatkowy kapitał, a nastepnie wydał 12 denarów. Potem
udał sie do Florencji, gdzie znowu podwoił liczbe posiadanych denarów i wydał 12. Po powrocie do Pizy po raz kolejny podwoił
swój majatek, wydał dwanaacie denarów i ... został bez grosza. Ile denarów miał na poczatku?
"""
# za pomoca petli for:
for i in range(0,1000):
    i=0.1*i
    print(i)
    if 2*(2*(2*i -12) - 12) - 12 == 0:
        print('kupiec na poczatku mial: ',round(i,2), ' denarow')

# za pomocą pętli while
i=1
while i<110:
    i = round(0.1 * i,2)


    if 2*(2*(2*i -12) - 12) - 12 == 0:
        print('kupiec na poczatku mial: ',round(i,2), ' denarow')
    i=i*10
    i+=1



# while False:
#     liczby =[]
#     i = random()*11
#     liczby.append(i)
#     for i in liczby:
#         if 2*(2*(2*i -12) - 12) - 12 == 0:
#             print('kupiec na poczatku mial: ',i, ' denarow')

# bin = "1011"
# print(int(bin, 2))



# print(random.uniform(20,60))
# # za pomoca petli while:


