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

#Write your code below this line 👇
list = [rock, paper, scissors]
print(
    "Welcome to the Rock, Paper, Scissors Game! Will you go home with a prize? Let's find out!"
)
user_rawchoice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
#To catch null entries:
if user_rawchoice == "":
    #Assume user choice is greater than 2, to prevent code from breaking.
    user_choice = 3
    print("Make a choice! Type 0 for Rock, 1 for Paper or 2 for Scissors.")
else:
    user_choice = int(user_rawchoice)

import random

comp_choice = random.randint(0, 2)
if user_choice == 0:
    if comp_choice == 1:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nYou lose. Try again!"
        )
    elif comp_choice == 2:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nYou win!"
        )
    else:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nIt's a draw! Try again."
        )
elif user_choice == 1:
    if comp_choice == 2:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nYou lose. Try again!"
        )
    elif comp_choice == 0:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nYou win!"
        )
    else:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nIt's a draw! Try again."
        )
elif user_choice == 2:
    if comp_choice == 0:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nYou lose. Try again!"
        )
    elif comp_choice == 1:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nYou win!"
        )
    else:
        print(
            f"You chose {list[user_choice]}\nComputer chose {list[comp_choice]}\nIt's a draw! Try again."
        )
elif int(user_choice) > 2:
    print("Pick a number between 0 and 2.")
