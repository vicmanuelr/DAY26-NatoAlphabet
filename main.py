import pandas as pd


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_entry = input("Enter a word: ").upper()
list_nato = [nato_dict[word] for word in user_entry]
print(list_nato)
