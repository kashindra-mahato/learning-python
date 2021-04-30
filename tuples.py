ups = 1, 2, 3, 4, 5
print(ups)
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'guy')
tuple3 = (tuple1, tuple2)
# concatenation
print(tuple1 + tuple2)
print(tuple3)
# slicing
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
# tuple cannot be updated
# tuple1[3] = 5
# print(tuple1)
# tuple lenght
print(len(tuple2))
# converting list into tuple
list1 = [0, 2, 3]
print(tuple(list1))
print(tuple('python'))
# use of double colon
var1 = "hello world"
print(var1[::-1])
# error due to a "comma"
tup = ('guy',)
n = 5
for _ in range(int(n)):
    tup = (tup,)
    print(tup)
tuple4 = ('kashindra', 'rajan', 'ramesh', 'rohan', 'ncit')
tuple5 = ('sagun', 'krishna', 'himalaya')

if tuple4 != tuple5:
    print('touples are not same')
else:
    print('same')

print('max element in tuples are' + ' ' + str(max(tuple4)) + ' ' + str(max(tuple5)))
print('min element in tuples are' + ' ' + str(min(tuple4)) + ' ' + str(min(tuple5)))

