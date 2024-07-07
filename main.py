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


option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choices = [0, 1, 2]

selected_option = random.choice(choices)



if option == 0:
    print(f"{rock}\nComputer chose:")
    if selected_option == 0:
        print(f"{rock}\nIt's a draw")
    elif selected_option == 1:
        print(f"{paper}\nYou lose")
    elif selected_option == 2:
        print(f"{scissors}\nYou win!")

elif option == 1:
    print(f"{paper}\nComputer chose:")
    if selected_option == 2:
        print(f"{scissors}\nYou lose")
    elif selected_option == 0:
        print(f"{rock}\nYou win!")
    elif selected_option == 1:
        print(f"{paper}\nIt's a draw")

elif option == 2:
    print(f"{scissors}\nComputer chose:")
    if selected_option == 1:
        print(f"{paper}\nYou win!")
    elif selected_option == 0:
        print(f"{rock}\nYou lose")
    elif selected_option == 2:
        print(f"{scissors}\nIt's a draw")
else:
    print("You typed an invalid number, you lose!")