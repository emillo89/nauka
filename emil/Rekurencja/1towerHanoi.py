'''1 (Wieże z Hanoi, Eduard Lucas, 1883). Mamy wieżę złożoną z n krążków, n ∈ IN0, ułożonych
jeden na drugim i nadzianych na jeden z 3 prętów (oznaczmy go przez A) malejącymi średnicami.
Zadanie polega na przeniesieniu całej wieży krążków na jeden z pozostałych prętów (oznaczmy
go przez B), przy czym w każdym ruchu można brać tylko jeden krążek i nie wolno położyć
większego krążka na mniejszym.
a) Ile co najmniej ruchów trzeba wykonać, aby przenieść wieżę?
b) Napisz program wyznaczający kolejne przełożenia dla klasycznego problemu wieży Hanoi.
c) Zapisz powyższy algorytm w postaci programu w dowolnym języku programowania. Program czyta ze standardowego wejścia nieujemną liczbę całkowitą n (liczba krążków) i wypisuje w kolejnych wierszach standardowego wyjścia kolejne przełożenia.
Przykład.
Dla danych wejściowych
3
poprawną odpowiedzią jest:
(A, B)
(A, C)
(B, C)
(A, B)
(C, A)
(C, B)
(A, B)'''

'''
Ad. a) ile trzeba wykonać ruchów: (2**n)-1
Ad. b) Napisz program:
'''
# def towerofHanoi(n, p1,p3,p2):
#     if n == 1:
#         print('Krazek z :', p1,3 ' na ',p3)
#         return
#     else:
#         towerofHanoi(n-1,p1,p2,p3)
#         print(n,' ', p1,' ', p3)
#         towerofHanoi(n-1, p2, p3,p1)
#
# towerofHanoi(4,'A','C','B')

'''
Ad. c)
'''

n = input('Ile krążków? ')
def tower_od_hanoi(n,p1,p3,p2):
    if n == 1:
        print(p1, " ",p3)
    else:
        tower_od_hanoi(n-1,p1,p2,p3)
        print(p1, " ",p3)
        tower_od_hanoi(n-1,p2,p3,p1)

print(tower_od_hanoi(3,'A','B','C'))