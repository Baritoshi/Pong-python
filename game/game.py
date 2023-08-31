import random

level = -1

while level  <= 0:

    try:

        level = int(input("Level: "))
    except ValueError:
        pass
    
number = random.randint(1, level)

while True:

    try:

        answer = int(input("Guess: "))

        if answer == number:
            print("Just right!")
            break
        elif answer < number:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        pass