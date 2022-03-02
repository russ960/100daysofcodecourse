import pandas

nato_alpha_csv = pandas.read_csv("./26/nato_phonetic_alphabet.csv")
nato_alpha_dict = {row.letter:row.code for (index,row) in nato_alpha_csv.iterrows()}

# My solution:
# nato_alpha_out = None
# while nato_alpha_out == None:
#     input_word = input("Enter a name: ").upper()
#     try:
#         nato_alpha_out = [nato_alpha_dict[letter] for letter in input_word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet.")

# Her solution:
def generate_phonetic():
    input_word = input("Enter a name: ").upper()
    try:
        nato_alpha_out = [nato_alpha_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet.")
        generate_phonetic()
    else:
        print(nato_alpha_out)

generate_phonetic()


