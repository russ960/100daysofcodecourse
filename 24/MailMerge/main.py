#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./24/MailMerge/Input/Letters/starting_letter.txt") as letter_file:
    base_letter = letter_file.read()
with open("./24/MailMerge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    new_letter = base_letter.replace("[name]", name.strip())
    with open(f"./24/MailMerge/Output/ReadyToSend/letter_for_{name.strip()}.txt", mode='w') as output_file:
        output_file.write(new_letter)
