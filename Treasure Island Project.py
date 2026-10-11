print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Imagine yourself in the middle of the outerspace.\nYou are standing on a random asteriod.\nTo reach the treasure, you have two ways. Either left or right.\nOn the left you see a big black abyss gulping space down and on the right you can see an endless path.")
direction = input("This is your chance to choose. Pick Left or Right.")

if direction == "Right" or direction == "right" :
    print("You are on the right path. Keep going until you come across a spaceship.")

    space_ship = input("Type Climb to board the space ship for your journey ahead.\nOr type Wait to wait in space")
        if space_ship == "Climb" or space_ship == "climb":
        print(
            "You have now arrived in a chamber with 3 doors.\n One is blue, and the other two are red and green colourd respectively.")
        elif space_ship == "Wait" or space_ship == "wait":
        print("Game over")
        else:
        print("Invalid input")
        colour = input("Choose a colour. The treasure lies behind one of the doors.")
            if colour == "Red" or colour == "red":
            print("Congratulations!!! You have found the treasure!!")
            else:
            print("Game over...Sorry you lose :(")

elif direction == "Left" or direction == "left" :
    print("Game over...Sorry you lose :(")
else :
    print("Not a valid input")

