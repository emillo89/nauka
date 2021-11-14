import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter : row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    name = list(input("Enter a word: ").upper())
    try:
        new_list = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()