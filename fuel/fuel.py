while True:
    try:
        fraction = input("prompt: ")
        prompt = fraction.split('/', maxsplit=1)
        x = int(prompt[0])
        y = int(prompt[1])
        if (x <= y):
            tank = x/y*100

            if (tank <=1):
                print("E")
                break
            elif (tank >= 99):
                print("F")
                break
            else:
                print(f"{round(tank)}%")
                break

    except (ValueError, ZeroDivisionError):
        pass





