import random


def guess_computer_number(x):
    
    print("Welcome to the game!")
    print(f"Choose a number between 1 and {x} for the computer to guess...") # 7

    limit_inf = 1
    limit_sup = x

    answer = ""
    intent = 0
    while answer != "c":
        intent += 1
        #Generar prediccion
        if limit_inf != limit_sup: # [1,10]
            prediction = random.randint(limit_inf, limit_sup)
        else:
            prediction = limit_inf # puede ser tambien el limit_sup

        # Get user answer
        answer = input(f"My prediction is {prediction}. If it is too big insert (A). If it is too small insert (B). If it is correct insert (C): ").lower()

        if answer == "a":
            limit_sup = prediction -1
        elif answer == "b":
            limit_inf = prediction + 1

    print(f"Computer guessed your number correctly: {prediction}. After {intent} intents.")


guess_computer_number(10)