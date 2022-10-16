# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads
print("\n Exercise 1 \n")

results = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count = 0
for result in results:
    if result == "heads":
        count += 1
print("Total number of heads are:", count)

# 2. Print square of all numbers between 1 to 10 except even numbers
print("\nExercise 2\n")

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i**2)

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
print("\nExercise 3\n")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
expenses = [2340, 2500, 2100, 3100, 2980]

your_expense = int(input("Enter your expense:"))

for expense in expenses:
    if your_expense == expense:
        index = expenses.index(your_expense)
        print(months[index])
        print(f"You spent {your_expense} for the month of {months[index]}")
        break

print(f"You spent {your_expense} for the month not available in the given list.")

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(5):
    print(f"You run {i + 1} kilometer(s)")
    tired = input("Are you tired?")
    if tired == 'yes':
        print("Sorry you didn't finish the race")
        break
if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
print("\nExercise 5\n")

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)

