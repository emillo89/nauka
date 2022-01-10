# Funcions can have inputs/funcionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Funcions are first-class objects

def calculate(name_function, n1, n2):
    return name_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

#Nested funcions

def outer_funcion():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_funcion()

#Funcions can be returned from other funcions
def outer_funcion():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_funcion = outer_funcion()
inner_funcion()
