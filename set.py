'''
# no repetitive elements
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 2, 1, 7}
print(set1)

set2 = {'a', 'b', 2, 'r', 1}

# union
set3 = set1 | set2
print(set1.union(set2))
print(set3)
set4 = set1 & set2

# intersection
print(set4)
print(set1.intersection(set2))

# adding and updating elements in set
set1.add(9)
print(set1)
set2.update([5, 4, 2])  # for multiple elements
print(set2)

# remove
set1.remove(7)
print(set1)

set1.discard(8)
print(set1)

# set1.remove(20)
# print(set1)

set1.discard(20)
print(set1)

print(set1.pop())
print(set1)

for i in range(10, 16):
    set1.add(i)
print(set1)
'''
a = set()
b = set()
n1 = int(input("Enter numbers of values in set a "))
n2 = int(input("Enter numbers of values in set b "))
for _ in range(n1):
    a.add(int(input("Enter values in set a: ")))
for _ in range(n2):
    b.add(int(input("Enter values in set b: ")))

print(a)
if a > b:
    print("set a is superset of set b")
elif a < b:
    print("set b is superset of set a")
elif a == b:
    print("both sets are equal")
else:
    print("neither of them are superset of other")

'''
print(set1 - set2)  # difference

a = {2, 4, 5, 6, 3}
b = {3, 6, 7}

if a.isdisjoint(b):
    print("TADAAA they are disjoint :)")
else:
    print(":(")

print(a.symmetric_difference(b))  # (a-b) U (b-a)
'''
