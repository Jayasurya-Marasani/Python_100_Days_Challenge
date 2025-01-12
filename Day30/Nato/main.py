import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_ok = True
while is_ok:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        is_ok = False
    except KeyError:
        print("Sorry only letters are allowed")
        is_ok = True
    else:
        print(output_list)
