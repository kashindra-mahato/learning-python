"""f = open('example1.txt', 'x')
f.write("This is my file\n Hello World")

f = open("example.txt", 'r')
print(f.read())
print(f.read(4))
print(f.read(10))
print(f.tell())
print(f.seek(4))
f.seek(0)
for line in f:
    print(line)

f.seek(0)
print(f.readlines())

import os

# os.rename("example1.txt","example.txt")

print(os.chdir("/home/kashindra/PycharmProjects"))
print(os.getcwd())
print(os.listdir("/home/kashindra/PycharmProjects"))
print(os.mkdir("test"))
"""
