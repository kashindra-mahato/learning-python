'''
mylist = []
#adding elements
mylist.append(1)
mylist.append(2)
mylist.append(3)
#printing the elements
print(mylist[0])
print(mylist[1])
print(mylist[2])

#loop
for x in mylist:
    print(x)

#concatenation
list = ['abcd',768,2.43,'john',70.2]
tinylist = [123,'john']
print(list[2:5])
print(tinylist*2) #tinylist printed twice
print(list+tinylist) #list and tinylist concatenated


#taking multiple input
x,y,z = [int(x) for x in input("enter three numbers: ").split()]  #plz watch :)
print(x,y,z)
'''


