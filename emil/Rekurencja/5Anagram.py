'''5. Podaj algorytm i napisz program, który opierajac sie na rekurencji wypisuje wszystkie anagramy
podanego słowa.
Wejscie. Program czyta ze standardowego wejscia. W pierwszym i jedynym wierszu podane
jest dowolne słowo o długosci ¬ 255.
Wyjscie: Program powinien wypisac w kolejnych wierszach standardowego wyjscia kolejne
anagramy badanego słowa wyjscie.
Przykład:
Dla danych wejsciowych:
abc
poprawna odpowiedzia jest:
abc
acb
bac
bca
cab
cba'''
def anagram2(text):
    tmp = []
    if len(text) == 0:
        return []
    elif len(text) == 1:
        return text
    elif len(text) < 256:
        for i in range(len(text)):
            litera = text[i]
            # print(litera)
            remain = text[:i] + text[i+1:]
            # print(i,remain)
            for j in anagram2(remain):
                tmp.append(litera + j)
                print(j,tmp)
        return tmp
print(anagram2('abc'))



# for i in range(len(text)):
#     tmp=[]
#     litera = text[i]
#     # print(litera)
#     remain = text[:i] + text[i + 1:]
#     print(i,remain)
#     for j in anagram2(remain):
#         tmp.append(litera + j)
#         # print(tmp)


# def anagram(text):
#     tab = list(text)
#     for i in tab:
#         for j in tab:
#             for k in tab:
#                 if i!=j and j!=k and i!=k:
#                     print(i+j+k)
#     print(tab)
#
# print(anagram('abc'))


