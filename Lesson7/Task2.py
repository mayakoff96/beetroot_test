# Input data:
# Compute the total price of the stock where the total price
# is the sum of the price of an item multiplied by the quantity of this exact item.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for item in stock:
    total_price += stock[item] * prices[item]

print('The total price of the stock is:', total_price)