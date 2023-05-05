print("This is a program that calculates how long you have till you turn 100 years old.\n")

name = input("What is your name? ")

while True:
    try:
        age = int(input("How old are you? "))
        if age == int:
            continue

    except ValueError:
        print("Please enter valid numbers")

    else:
        age100 = 100 - age
        year = age100 + 2023

        print()
        print(name, "you will be at the age of 100 in the year", year, "\n")
        print("You have", age100, "years left till you turn 100. \n\nHappy 100 years to you in", age100, "years.\n\n\n")
        break
