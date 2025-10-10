'''

 "SNAKE WATER GUN GAME"

 <--:RULE OF THIS GAME:-->
 1. Snake vs. Water: Snake drinks the water hence Snake wins.
 2. Water vs. Gun: The gun will drown in water, hence a point for water
 3. Gun vs. Snake: Gun will kill the snake and Gun win.

'''

import random

computer_choice = random.choice([-1, 0, 1])
user_choice = input("Enter your choice out of (snake, water, gun): ")


conversion_of_codeDigit_to_choice = {
    -1: "snake",
    0: "water",
    1: "gun"
}

conversion_of_choice_to_codeDigit = {
    "snake": -1,
    "water": 0,
    "gun": 1
}

user_digit_choice = conversion_of_choice_to_codeDigit[user_choice]
print(f"You chose {user_choice} and Computer chose {conversion_of_codeDigit_to_choice[computer_choice]}")


if (computer_choice == user_digit_choice):
    print("Match Draw.")
else:
    if (computer_choice == -1 and user_digit_choice == 0):
        print("You lose.")
    elif (computer_choice == -1 and user_digit_choice == 1):
        print("You Win!")
    elif (computer_choice == 0 and user_digit_choice == -1):
        print("You Win!")
    elif (computer_choice == 0 and user_digit_choice == 1):
        print("You lose.")
    elif (computer_choice == 1 and user_digit_choice == -1):
        print("You lose.")
    elif (computer_choice == 1 and user_digit_choice == 0):
        print("You Win!")
