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

def calculator():
    num1 = int(input("What's the first number? "))


    for key in operations:
        print(key)

    question = True

    while question:

        operation_symbol = input("Pick an operation: ")

        num2 = int(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        your_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit, or 'i' to start new calculation: ")
        if your_choice == 'y':
            num1 = answer
        elif your_choice == 'i':
            calculator()
        else:
            question = False

calculator()