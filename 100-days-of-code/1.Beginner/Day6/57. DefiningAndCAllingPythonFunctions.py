

#create own function

def my_function():
    print('Hello')
    print('Bye')


#Reeborg's World
suma = 0
def turn_left():
    global suma
    suma += 1
    print(suma)

turn_left()
print(suma)


# def turn_around():
#     tern_left()