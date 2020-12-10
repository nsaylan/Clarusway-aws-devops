word= input("Please enter a string: ")

def consecutive(word):
    all=["a","e","i","o","u"]
    m=0
    result = False
    while m < (len(word)-1):
        for x in all:
            for y in all:
                if (x == word[m]) and (word[m+1] == y):
                    result = True
                    print("Positive")
                    break
                else:
                    continue
        m+=1
    if not result:
        print("Negative")
consecutive(word)

        
        
        
        
        
        
                   

