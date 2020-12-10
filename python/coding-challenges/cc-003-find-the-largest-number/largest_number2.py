lst = []
for n in range(5):
    number = int(input('Enter number '))
    lst.append(number)

lst.sort()
print("The largest number:", lst[-1])