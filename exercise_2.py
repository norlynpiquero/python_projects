#1
length = 92
width = 48.8
area = length*width
print("area of football field is: ",area)

#2  You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
cost_per_packet = 1.49
number_of_packets = 9
total_cost = cost_per_packet * number_of_packets
change = 20 - total_cost
print(change)

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
length = 5.5
area = length**2
cost = 500 * area
print("The total cost for bathroom",cost)

# 4. Print binary representation of number 17
num = 17
print("The binary of number 17 is",format(num,'b'))
