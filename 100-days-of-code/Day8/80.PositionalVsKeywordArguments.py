# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet_with_name(name):
#     print('My functions')
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name('Emil')

#def grret_with_name(name='Emil') name = jest parametrem, Emil = argumentem

#Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#Functions with keyqord arguments
greet_with(location = 'Lublin', name = 'Emil')

