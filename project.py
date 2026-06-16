print("Welcome")

a = int(input("Insert card (1 = yes, 2 = no): "))

if a == 1:
    print("card accepted")

    b = int(input("Enter the pin: "))

    if b == 2345:
        print("pin is correct")

    else:
        print("Wrong PIN")


else:
    print("Card not accepted")

c=int(input("select the language(1.kannada,2.english,3.telugu): "))
if c == 1:
    print("kannada accepted")
elif c == 2:
    print("english accepted")
else:
    print("telugu accepted")

d=int(input("Balance acc "))
if d == 9000:
    print("balance is correct")
else:
    print("wrong balance")

e=int(input("withdrawal: "))
if e == 10000:
    print("withdrawal is correct")
else:
    print("wrong balance")
    

