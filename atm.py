from typing import Text
 
balance =50000
d =0
while d < 1:
    #name is nicky
    #passcode is 5763
    print("welcome!")
    n=input("enter name: ")
    if(n=="nicky"):
        n=input("enter passcode: ")
        if(n=="5763"):
            print("account balance is £")
            print(balance)
            n=input("would you like to |{A} take out money||{B} put in money||{C} exit||{D} logout| ")

            if(n=="A"):
                n=int(input("how much would you like to take out?: "))
                balance = balance-n
                print("new balance £")
                print(balance)
                
            if(n=="B"):
                n=int(input("how much would you like to put in?: "))
                balance += n
                print("new balance £")
                print(balance)
                
            if(n=="C"):
                d+=1
            




        else:
            print("passcode incorrect")
            n=input("would you like to leave?y/n: ")
            if(n=="y"):
                d+=1
    else:
        print("name incorrect")
        n=input("would you like to leave?y/n: ")
        if(n=="y"):
            d+=1
    
