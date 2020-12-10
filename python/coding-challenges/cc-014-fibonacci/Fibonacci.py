nterms = int(input("How many fibonacci numbers would you like to generate? "))

n1, n2 = 0, 1
count = 0
list = []
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print(n2)
else:
    while count < nterms:
       list.append(n2)
       n = n1 + n2
       n1 = n2
       n2 = n
       count += 1
    print(list)