a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourht number:"))
e = int(input("Enter the fifth number:"))

if a > b and a > c and a > d and a > e:
    print(a, "is the largest number")
elif b > a and b > c and b > d and b > e:
    print(b, "is the largest number")
elif c > a and c > b and c > d and c > e:
    print(c, "is the largest number")
elif d > a and d > b and d > c and d > e:
    print(d, "is the largest number")
else:
    print(e, "is the largest number")