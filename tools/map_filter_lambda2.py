names = []

while True:
    num = input("Enter a number if want to exit enter exit: ")
    if num == "exit":
        break
    names.append(num)


hight_names = list(filter(lambda x: len(x)>=5, names))
hight_names_los= list(filter(lambda x: len(x)<5, names))


print("نام هایی با بیش تر از 5 حرف")
print(hight_names)
print("نام هایی با کمتر از 5 حرف")
print(hight_names_los)