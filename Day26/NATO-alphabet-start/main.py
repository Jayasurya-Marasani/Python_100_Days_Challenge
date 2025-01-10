import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}


df = pandas.read_csv("nato_phonetic_alphabet.csv")

words_dict = {row.letter : row.code for (index, row) in df.iterrows()}

# words_dict = {row['letter'] : row['code'] for (index, row) in df.iterrows()}
# print(words_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word:").upper()

letters = [letter for letter in word]

# for letter in letters:
#     print(words_dict[letter])

phonetic_words = [words_dict[letter] for letter in letters]

print(phonetic_words)