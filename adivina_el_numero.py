import random

def guess_the_number(x):

    print("Welcome to the game")
    print("You are supposed to guess the number")

    random_num = random.randint(1, x) #random integer between 1 and x.

    prediction = 0

    while prediction != random_num:
        prediction = int(input(f"Guess a number between 1 and {x}: ")) # f-string

        if prediction < random_num:
            print("Try again. THis number is too small.")
        elif prediction > random_num:
            print("Try again. This number is too big.")

    print(f"Congrats! You guessed the number {random_num} correctly.")


guess_the_number(10)
     

