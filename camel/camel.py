camelCase = str(input("Camel Case: "))
snake_case = ""

for letter in range(len(camelCase)):
    if camelCase[letter].isupper():
        snake_case += "_"
        snake_case += camelCase[letter].lower()
    else:
        snake_case += camelCase[letter]

print("Snake Case:", snake_case)