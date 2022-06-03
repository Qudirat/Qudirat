choice1 = input(
    "Welcome to Treasure Island!\nYou're at a crossroad. Where do you want to go? Type 'left' or 'right'?\n"
).lower().strip()
if choice1 == 'left':
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
    ).lower().strip()
    if choice2 == 'wait':
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
        ).lower().strip()
        if choice3 == 'yellow':
            print("You found the treasure! You Win!")
        elif choice3 == 'red' or choice3 == 'blue':
            import random
            lose_statements = [
                "It's a room full of fire. Game Over.",
                "You enter a room of beasts. Game Over.",
                "You get attacked by an angry trout. Game Over.",
                "You get attacked by an angry trout. Game Over."
            ]
            print(random.choice(lose_statements))
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif choice2 != 'wait':
        print("A trout jumps out and swallows you! Game over.")
elif choice1 != 'left':
    print('You fell into a hole! Game over.')