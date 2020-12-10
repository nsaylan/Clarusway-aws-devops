
milis =input("Please enter the milliseconds (should be greater than zero)(To exit the program, please type 'exit'): ")
while True:
    if milis == "exit":
        print("Exiting the program... Good Bye")
        break
    try:
        milis=int(input("Please enter the milliseconds (should be greater than zero)(To exit the program, please type 'exit'): "))
    except ValueError:
        print("Not Valid Input !!!")
        continue
    if int(milis) <= 0:
        print("Not Valid Input !!!")
    elif int(milis) == 1:
        milis=input("Please enter the milliseconds greater than 1 : ")
        continue   
    else:
        seconds=(int(milis)/1000)%60
        minutes=(int(milis)/(1000*60))%60
        hours=(int(milis)/(1000*60*60))%24
        print ("%d:%d:%d" % (hours, minutes, seconds))