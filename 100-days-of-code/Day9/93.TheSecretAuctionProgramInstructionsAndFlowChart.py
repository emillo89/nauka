# from replit import clear
#HINT: You can call clear() to clear the output in the consol



from art import logo

print(logo)
dictionary = {}

want = True

while want:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    dictionary[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if should_continue == 'no':
        want = False

        max = 0
        for key in dictionary:

            if dictionary[key] > max:
                person = key
                max = dictionary[key]

        print(f"You are a winner: {person}, Your bid is: ${max}")
        print(dictionary)