import random

true_number = random.randint(1, 50)
true_number
user_number = int(input("Enter your guess between 1 to 50: "))

while True:
    if user_number == true_number:
        print("You got it right!")
        break
    elif user_number > true_number:
        print("Your guess number is high, try again.")
        user_number = int(input("Enter your guess between 1 to 50: "))
    elif user_number < true_number:
        print("Your guess is low, try again")
        user_number = int(input("Enter your guess between 1 to 50: "))


user_number