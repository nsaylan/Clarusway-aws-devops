name=input("Please enter your full name(without any space): ").lower()
import random
result=[]
def get_random_letter():
    for i in range(3):
        letter= random.choice(name)
        result.append(letter)
    print(result, end='')
get_random_letter()
print(random.randrange(1000, 10000))
    
    