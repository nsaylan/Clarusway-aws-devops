n=int(input("Please enter the side length of the box:"))
if n == 1:
  print("#")
else:
  print("#"*n)
  for i in range(n-2):
    print("#"," "*(n-4),"#")
  print("#"*n)
    

