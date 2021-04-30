#day2
''''#string operations
a = "Hello, World"
b = a.lstrip() #strips the space from left
c = a.rstrip()
print(len(b))
print(len(c))
print(a.lower())
print(a.upper())
print(a.replace("H","j"))
print(a.split(","))
a1 = 'my name is kashindra'
print(a1.split(' '))

#input

print('Enter your name:')
x= input()
print('Hello ',x)
x1 = input('Enter your name: ')

#next line
print("\nHello, ",x)

#stringoperation
str = 'holy himalaya'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str *2)
print(str + "test")

#separator
print('Hello','World',sep = "...")

#variables that store different data type, can be defined
#also called chain variable
a,b,c = 'hi',5,2.89
print(a,b,c)


name = input('Enter your name')#'kashindra'
age = int(input('enter your age'))#21
print('Hello %s ! Are you %d yrs old?'%(name,age))

print('marks = %.2f'%92.5)


value = float(input("Enter a number:"))
value1 = float(input('enter a number:'))
print("Highest value is: ",max(value,value1))


x,y = input("Enter two values: ").split()
print('number of boys: ',x)
print('number of girls: ', y)
'''
#day3
'''
x,y,z = input("Enter three values: ").split()
print(int(x)+int(y)+int(z))
print("value of x is {} value of y is {}".format(x,y))
print(f"value of x is {x} value of y is {y}") #f does the work of format
'''
