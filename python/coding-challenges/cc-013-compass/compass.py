dir=input("Enter the starting direction: ")
if dir == 'N':
    dir == 0
elif dir == 'E':
    dir == 1
elif dir == 'S':
    dir == 2
elif dir == 'W':
    dir == 3
i=0
n=int(input("How many direction will you enter:"))
while i in range(n):
    move=input("Which direction? ")
    if move == 'R': 
       dir == (int(dir) + 1)
    elif move == 'L': 
        dir == (4 + int(dir) - 1)

print("Last direction: dir")