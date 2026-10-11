import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock , paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice <= 2 and player_choice >= 0:
    print(game[player_choice])
else :
    print("Invalid input")


print("Computer chose:")

random_comp_choice = random.randint( 0 , 2 )
print(game[random_comp_choice])


#METHOD 1 - FOR THIS THE random_comp_choice == 3, 4, 5
# if random_comp_choice == 3 and player_choice == 0:
#     print("It's a draw")
# elif random_comp_choice == 4 and player_choice == 1:
#     print("It's a draw")
# elif random_comp_choice == 5 and player_choice == 2:
#     print("It's a draw")
# elif random_comp_choice == 3 and player_choice == 1:
#     print("You win")
# elif random_comp_choice == 3 and player_choice == 2:
#     print("You lose")
# elif random_comp_choice == 4 and player_choice == 0:
#     print("You lose")
# elif random_comp_choice == 4 and player_choice == 2:
#     print("You win")
# elif random_comp_choice == 5 and player_choice == 0:
#     print("You win")
# elif random_comp_choice == 5 and player_choice == 1:
#     print("You lose")
# else:
#     print("Invalid input")


#METHOD 2 -

if player_choice < 0 or player_choice >2:
    print("You lose")
elif player_choice == random_comp_choice:
    print("It's a draw")
elif player_choice == 2 and random_comp_choice == 0 or player_choice == 1 and random_comp_choice == 2 or player_choice == 0 and random_comp_choice == 1:
    print("You lose")
elif player_choice == 1 and random_comp_choice == 0 or player_choice == 0 and random_comp_choice == 2 or player_choice == 2 and random_comp_choice == 1:
    print("You win")
