amount = 50
print (f"Amount Due: {amount:.0f}")
while (amount > 0):
    coin = int(input("Insert Coin: "))
    if (coin == 50 or coin == 25 or coin == 10 or coin == 5):
        amount = amount - coin
    if (amount > 0):
        print (f"Amount Due: {amount:.0f}")
    elif (amount <= 0):
        print (f"Change Owed: {abs(amount):.0f}")