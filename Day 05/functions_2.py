prices_coffee = [('express', 10), ('heavy', 10.2), ('mocha', 5), ('capuccino', 50.2)]


def expensive_coffee(myList):
    price_expensive = 0
    coffee_expensive = ''

    for coffee, price in myList:
        if price > price_expensive:
            price_expensive = price
            coffee_expensive = coffee
        else:
            pass

    return coffee_expensive, price_expensive


coffee, price = expensive_coffee(prices_coffee)
print(f"The coffee expensive is {coffee} and the price is {price}")
