import pandas

input_word = input("Enter a name: ").upper()

nato_alpha_csv = pandas.read_csv("./26/nato_phonetic_alphabet.csv")
nato_alpha_dict = {row.letter:row.code for (index,row) in nato_alpha_csv.iterrows()}

nato_alpha_out = [nato_alpha_dict[letter] for letter in input_word]

print(nato_alpha_out)


