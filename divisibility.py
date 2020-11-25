#divisibility.py
#Divisibility program for CSCI 111-900
#Last edited 10/14/19 by Pat Doyle

def divisibility(x,y):
    if (x % y == 0):
        print("Multiple of ", y , )

    #Function evaluates if x is divisibile by y

num = 1

while (num <= 25):
    print(num)
    divisibility(num, 2)
    divisibility(num, 3)
    divisibility(num, 5)
    num += 1

    #While loop prints numbers 1 to 25 and tests divisibility by 2, 3, and 5.
