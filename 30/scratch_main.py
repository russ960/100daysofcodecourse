# FileNotFound
 
# with open("a_file.txt") as file:
#     data = file.read()
# try:
#     file = open("a_file.txt")
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except NameError:
#     print("That key does not exist")
# else: 
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File")
#     raise TypeError("My made up error")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3m.")

bmi = weight / height**2
print(bmi)