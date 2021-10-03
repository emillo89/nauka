from art import logo


#Calculator
print(logo)
#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    if n2 == 0:
        print()
    return n1 / n2


operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
}

num1 = int(input("What's the first number? "))


for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number? "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)



print(f"{num1} {operation_symbol} {num2} = {answer}")