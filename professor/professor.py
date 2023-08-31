import random


def main():
    #...

    level = get_level()
    score = 0
    chances = 3
    for i in range(10):
        #get numbers
        number1 =  generate_integer(level)
        number2 = generate_integer(level)
        #ask for math problem
        while True:
            try:

                answer = input(str(number1) + " + " + str(number2) + " = ")
            #compare answer with real answer and give point
                if int(answer) == int(number1) + int(number2):
                    score += 1
                    break
                else:
                    print ("EEE")
                    chances -= 1
                    if chances < 1:
                        sum = int(number1) + int(number2)
                        print(str(number1) + " + " + str(number2) + " = " + str(sum))
                        break
            except ValueError:
                print ("EEE")


    print("Score: " + str(score))




def get_level():
    #...

    n = -1
    while True:
        try:

            n = int(input("Level: ")) #get level number

            if  1 <= n <= 3:
                break
        except ValueError:
            pass
    return n



def generate_integer(level):
    #...
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10,99)

    else:
        number = random.randint(100,999)
    return number



if __name__ == "__main__":
    main()
