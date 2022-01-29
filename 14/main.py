from art import logo, vs
from game_data import data
from random import randint
#from replit import clear

def get_comp_person(current_b_value, previous_comp_values):
 num_persons =  len(data)-1
 person = randint(0,num_persons)
 while person == current_b_value or person in previous_comp_values:
   person = randint(0,num_persons)
 return person

game_end = False
compare_a = None
compare_b = None
score = 0
print(logo)

previous_comparisons = []
while not game_end:

  if compare_a == None:
    # First run choose a new value to compare.
    compare_a = get_comp_person(None, previous_comparisons)
  compare_b = get_comp_person(compare_b, previous_comparisons)

  while compare_a == compare_b:
    compare_b = get_comp_person(compare_b, previous_comparisons)
  #print(f"{compare_a} : {compare_b}")
  #print("{} : {}".format(data[compare_a]["follower_count"], data[compare_b]["follower_count"]))
  print("Compare A: {}, a {}, from {}.".format(data[compare_a]["name"],data[compare_a]["description"], data[compare_a]["country"]))

  print(vs)

  print("Compare A: {}, a {}, from {}.".format(data[compare_b]["name"],data[compare_b]["description"], data[compare_b]["country"]))

  previous_comparisons.append(compare_a)
  previous_comparisons.append(compare_b)

  selected_comparison = (input("Who has more followers? Type 'A' or 'B': ")).lower()
  correct_comparison = None
  if data[compare_a]["follower_count"] == data[compare_b]["follower_count"]:
    correct_comparison = True
    if selected_comparison == 'b':
      compare_a = compare_b
  elif data[compare_a]["follower_count"] > data[compare_b]["follower_count"]:
    if selected_comparison == 'a':
      correct_comparison = True
    else:
      correct_comparison = False
  elif data[compare_a]["follower_count"] < data[compare_b]["follower_count"]:
    if selected_comparison == 'b':
      correct_comparison = True
      compare_a = compare_b
    else:
      correct_comparison = False
  if correct_comparison == True:
    score += 1
    #clear()
    print(logo)
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}.")
    game_end = True