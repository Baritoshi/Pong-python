expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
match(y):
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        if z != 0:
            print(x / z)
        else:
            print("You can't divide by zero!")
    case _:
        print("Try again")
