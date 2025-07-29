numbers = []

while True:
    num = int(input("Enter a number, if want to exit from this program enter zero: "))
    if num == 0:
        break
    numbers.append(num)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

if even_numbers:
    total = sum(map(lambda x: x, even_numbers))
    average = total / len(even_numbers)
    print("The average area of the even numbers is:", average)
else:
    print("No even numbers found")
