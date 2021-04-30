'''
x,y = 30
if (x>30):
    print("i am in if")
elif(x>25):
    print("im not in if")
else:
    print("i am neither")

x,y = input("Enter two values").split()
x = int(x)
y= int(y)
if(x+y>100):
    print("sum: {} is greater than 100".format(x+y))
else:
    print("The sum is lesser than 100")
'''

#nested if statements
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = a + b
if(c>0):
    if(c%2 == 0):
        print("The sum {} is even".format(c))
    else:
        print("The sum {} is odd".format(c))

