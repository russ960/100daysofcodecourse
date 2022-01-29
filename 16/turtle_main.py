# import turtle

# russ = turtle.Turtle()
# russ.shape("turtle")
# russ.color("blue4")
# russ.fd(100)
# myscreen = turtle.Screen()
# myscreen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = 'l'
print(table)