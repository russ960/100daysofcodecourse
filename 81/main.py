from morse_code import morse_code_alphabet as mca

text_string = (input("Please enter the string you need converted to morse code: ")).upper()
translated_string = ""

for letter in text_string:
    try:
        morse_letter = mca[letter]
    except KeyError:
        morse_letter = '#'
    if letter == ' ':
        translated_string += f"/ "
    else:
        translated_string += f"{morse_letter} "
print(f"Here is your translated string: \n{translated_string}")