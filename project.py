#import random
print("Welcome! You will select a color and a number and I will tell you your future.")

answer = "y"

while answer == "y":
    color = input("Select a color [yellow, green,blue, red]")

    if color == "yellow" or color == "green":
        number = int(input("Select a number between [1, 2, 5, 6]"))
        if number == 1:
            print("Your dreams will come true but be patient!")
        elif number == 2:
            print("You will become a millionaire when you turn 85")
        elif number == 5:
            print("You will have 10 kids in the future")
        elif number == 6:
            print("You will become famous!")
        else:
            print("You entered a number that is not allowed.")

    elif color == "blue" or color == "red":
        number = int(input("Select a number between [3, 4, 7, 8]"))

        if number == 3:
            print("You will live a happy life.")
        elif number == 4:
            print("You will marry a super rich man/woman")
        elif number == 7:
            print("You will die early but happy")
        elif number == 8:
            print("You will win in a lottery")
        else:
            print("You entered a number that is not included in the choices.")

    answer = input("Do you want to play the game again? Type 'y' for YES and 'n' for NO:")
