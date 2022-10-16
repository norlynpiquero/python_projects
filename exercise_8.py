"""
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for four type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
"""
population_dict = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}

def add():
    country = input("Enter a country name to add:").lower()

    if country in population_dict:
        print("Country already exist in the dataset.")
        return
    population = input(f"Enter the population of the {country} you just entered")
    population = float(population)

    population_dict[country] = population
    print_all()

def remove():
    country = input("Enter name of country to remove from the dataset").lower()

    if country not in population_dict:
        print("This country doesn't exist in the dataset so no need to remove.")
        return

    del population_dict[country]
    print_all()

def query():
    country = input("Enter country to query:").lower()
    if country not in population_dict:
        print("This country doesn't exist in the dataset.")
        return
    print(f"Population of the country you just entered is {population_dict[country]}")

def print_all():
    for country, population in population_dict.items():
        print(f"{country} ==> {population}")

def ask():
    operation = input("Enter operation (add, remove, query or print):").lower()

    if operation == "add":
        add()
    elif operation == "remove":
        remove()
    elif operation == "query":
        query()
    elif operation == "print":
        print_all()

ask()

