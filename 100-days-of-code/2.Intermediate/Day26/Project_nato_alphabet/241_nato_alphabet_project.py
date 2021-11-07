import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter : row.code
    for (index, row) in data.iterrows()
}

#Create a list of the phonetic code word that the user inputs
name = list(input("Enter a word: ").upper())
print(name)
new_dict ={letter : code
    for (letter, code) in data_dict.items() if letter in name
}
new_list = [new_dict[letter] for letter in name]
print(new_dict)
print(new_list)
