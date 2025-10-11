# We are going to write a program that generates a random number between 0 to 100  and asks the user to guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number. 


import random

random_number = random.randint(0, 100)
user_number = int(input("Guess the Random number in [0, 100]: "))

count = 1
while (random_number != user_number):
    if (user_number > random_number):
        user_number = int(input("Guess the lesser number please: "))
    else:
        user_number = int(input("Guess the higher number please: "))
    count += 1
else:
    print(f"Congratulation🎉, you guess the random number in {count} tries!🎖️")


