'''*args - oznacza nieskonczona ilosc argumentow funkcji
**kwargs odnosi sie do slownika'''

def funkcja(arg1,arg2, *args,**kwargs):
    print(arg1,arg2,args,kwargs)

funkcja('Jacek','cos','!','***', author='Sebastian')