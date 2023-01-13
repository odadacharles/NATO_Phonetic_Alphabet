import pandas as pd

phonetic_DF = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dic = {row.letter: row.code for (index, row) in phonetic_DF.iterrows()}


def generate_phonetic():
    user_input = input("Please enter a word: ").lower()
    letters = [letter.upper() for letter in user_input]
    try:
        word_code = [phonetic_dic[letter] for letter in letters]
    except KeyError:
        print("Letters Only")
        generate_phonetic()
    else:
        print(word_code)


generate_phonetic()
