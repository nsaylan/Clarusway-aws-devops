#try:
#    num1=7
#    num2=1
#    print(num1/num2)
#    print("done calculation")
#except ZeroDivisionError:
#    print("an error occured")
#    print("due to zero division")

# ********
#try:
#    variable = 10
#    print(variable + "hello")
#    print(variable/2)
#except ZeroDivisionError:
#    print("divided by zero")
#except (ValueError, TypeError):
#    print("error occured")

# ***
#try:
#    word = "spam"
#    print(word / 0)
#except:
#    print("an error occured")

# ****
#try:
#    print("hello")
#    print(1 / 0)
#except ZeroDivisionError:
#    print("divided by zero")
#finally:
#    print("this code will run no matter what")
#try:
#  print(1)
#  print(10 / 0)
#except ZeroDivisionError:
#  print(unknown_var)
#finally:
#  print("this is executed last")

# *****
#print(1)
#raise ValueError
#print(2)

# ******
#name = "123"
#raise NameError("invalid name!")

# *******
#try:
#    num = 5 / 0
#except:
#    print("an error occured!")
#    raise

# ********
#print(1)
#assert 2+2==4
#print(2)
#assert 1+1==3
#print(3)
#assert 1+2==3
#print(4)

# *********
temp = -10
assert (temp >=0), "colder than zero"