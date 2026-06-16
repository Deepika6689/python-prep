import time
balance=10000
password=2345
print("welcome")
print("insert the card")
a=int(input("card? 1.yes,2.no"))
if a == 1:
    print("card is inserted")
    b=int(input("enter the pin:"))
    if b == password:
        print("password is correct")
        c=int(input("selecte the language: 1.kannada,2.english,3.telugu"))
        if c == 1:
            print("kannada is correct")
        elif c == 2:
            print("english is correct")
        elif c == 3:
            print("telugu is correct")
        print("1.balance")
        print("2.withdrawal")
        choice=int(input("enter your choice:"))
        if choice == 1:
            print("your balance is :",balance)
        elif choice == 2:
            amt=int(input("amount u want to withdraw:"))
        if amt <= balance:
            print("your transaction is being processed:")
            time.sleep(5)
            balance -= amt
            print("collect ur cash")
            time.sleep(5)
            check=int(input("do u want to check the balance: 1.yes,2.no"))
            if check == 1:
                print("your remaining balance is :",balance)
            else:
                print("thank you ")
        else:
            print("invalid option")
    else:
        print("password is incorrect")
else:
    print("card is not inserted")