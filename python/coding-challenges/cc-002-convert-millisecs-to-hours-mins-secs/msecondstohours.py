###  This program converts milliseconds into hours, minutes, and seconds ###
while True:
    ms = input("To exit the program, please type 'exit'. Please enter the milliseconds (should be greater than zero) :")
    if ms.lower()=="exit":
        print("Exiting the program... Good Bye")
        break
    elif not ms.isdigit() or int(ms) <= 1:
            print("Not Valid Input !!!")
    else:
        while ms.isdigit() == True: 
            if int(ms) <=999:
                print(f"Just {ms} miliseconds")
                break
            elif int(ms) >= 1000:
                hour = int(ms) // 3600000
                minute = (int(ms) % 3600000) // 60000
                second = (int(ms) % 60000) // 1000
                result = {hour: "hour/s", minute: "minute/s", second: "second/s"}
                for x, y in result.items():
                    if x > 0:
                        print(x, y, end=" ")
                break
        break
    

    



