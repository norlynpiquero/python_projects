# Python Projects

These contains all the exercises and projects I did in learning the basics of Python using the free resources online; Udemy and YouTube.

<h1>Project_1:</h1>
This is a guessing game where you ask the user to input a number between 1 to 50 and the computer will generate a random number between those numbers. The program will output a result according to the user's input.

<h1>Project_2 (*project):</h1>
This is a fortune telling game where you ask the user to input a color and number. The chosen color and number have corresponding meaning which the computer will return as an output.

<h1>Project_3 (project_3):</h1>
This program will give you your zodiac sign. It will ask for your year, month and date of birth.

<h1>exercise_1: Variables</h1>
1. Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.
2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables
3. Store your first, middle and last name in three different variables and then print your full name using these variables
4. Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue

<h1>exercise_2: Numbers</h1>
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
4. Print binary representation of number 17

<h1>exercise_3: String</h1>
1. Create 3 variables to store street, city and country, now create address variable to
store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line
2. Create a variable to store the string "Earth revolves around the sun"
    1. Print "revolves" using slice operator
    2. Print "sun" using negative index
3. Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
4. I have a string variable called s='maine 200 banana khaye'. This of course is a
wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string.
Also try to do this in one line.

<h1>exercise_4: Lists</h1>
1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this

2. You have a list of your favourite marvel super heros.
```
heros=['spider man','thor','hulk','iron man','captain america']
```

Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
       so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

<h1>exercise_5: If condition</h1>
1. Using following list of cities per country,
    ```
    india = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan = ["lahore","karachi","islamabad"]
    bangladesh = ["dhaka", "khulna", "rangpur"]
    ```
    1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
    2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
    1. Ask user to enter his fasting sugar level
    2. If it is below 80 to 100 range then print that sugar is low
    3. If it is above 100 then print that it is high otherwise print that it is normal
   
<h1>exercise_6: Loop</h1>
 1. After flipping a coin 10 times you got this result,
```
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
```
Using for loop figure out how many times you got heads

2. Print square of all numbers between 1 to 10 except even numbers
3. Your monthly expense list (from Jan to May) looks like this,
```
expense_list = [2340, 2500, 2100, 3100, 2980]
```
Write a program that asks you to enter an expense amount and program
should tell you in which month that expense occurred. If expense is not
found then it should print that as well.

4. Lets say you are running a 5 km race. Write a program that,
   1. Upon completing each 1 km asks you "are you tired?"
   2. If you reply "yes" then it should break and print "you didn't finish the race"
   3. If you reply "no" then it should continue and ask "are you tired" on every km
   4. If you finish all 5 km then it should print congratulations message

5. Write a program that prints following shape
```
*
**
***
****
*****
```

<h1>exercise_7: Functions</h1>
1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
```
area = (1/2)*base*height
```

2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
```
rectangle area=length*width
```
If no shape is supplied then it should take triangle as a default shape

3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
```
*
**
***
```
if input is 4 then it should print
```
*
**
***
****
```
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

<h1>exercise_8, exercise_8.1, exercise_8.2:</h1>
These are about reading and manipulating the data give. The problems/questions can be read on each exercises.
