"""
You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
"""

import statistics

stocks = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}

def print_all():
    for stock_ticker, stock_list in stocks.items():
        avg = statistics.mean(stock_list)
        print(f"{stock_ticker} ==> {stock_list} ==> avg: ", round(avg, 2))

def add():
    stock_ticker = input("Enter the stock ticker you want to add:")
    stock_price = input("Enter the stock price:")
    stock_price = float(stock_price)

    if stock_ticker in stocks:
        stocks[stock_ticker].append(stock_price)
    else:
        stocks[stock_ticker] = stock_price
    print_all()

def ask():
    operation = input("Enter operation (print or add):")

    if operation == "print":
        print_all()
    elif operation == "add":
        add()
    else:
        print("Unsupported operation:", )

ask()


