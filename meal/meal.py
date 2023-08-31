def main():
    time = input("What time is it? ")
    mealtime = convert(time)
    if mealtime >= 7.0 and mealtime <= 8.0:
        print("breakfast time")
    elif mealtime >= 12.0 and mealtime <= 13.0:
        print("lunch time")
    elif mealtime >= 18.0 and mealtime <= 19.0:
        print("dinner time")




def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    hours = float(hours) + minutes
    return hours

if __name__ == "__main__":
    main()
