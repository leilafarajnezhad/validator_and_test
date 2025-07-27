def price_object():
    try:
        price = float(input("Enter price in dollars: "))
        if 1000 <= price <= 2000:
            print("The price is valid:", price)
            return price
        else:
            print("The price must be between 1000 and 2000 dollars.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

assert price_object() == None
assert price_object() == 1000
assert price_object() == 2000
assert price_object() == 3000
