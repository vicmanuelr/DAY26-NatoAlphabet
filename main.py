import pandas as pd


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato():
    user_entry = input("Enter a word: ").upper()
    try:
        list_nato = [nato_dict[word] for word in user_entry]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_nato()
    else:
        print(list_nato)


generate_nato()
