groceryList = {}

while True:
    try:
        item = input().upper()
        if item not in groceryList:
            groceryList[item] = 1
        else:
            groceryList[item] +=1

    except EOFError:
        for key, value in sorted(groceryList.items()):
            print(value, key)
            pass
        break
    except KeyError:
        pass

