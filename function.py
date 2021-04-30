'''
# build in function

num = -100
print (abs (num))  # abs()

list = [1, 2, 3]

print (all (list))  # all()
# True
list = [0, 1, 2]  # 0 present
print (all (list))
#False

numbers = dict ()

print (dir (numbers))
# prints out probable functions present in numbers

print (divmod (9, 2))  # print quotient and remainder as a tuple

numbers = [10, 20, 30, 40]
for i, n in enumerate (numbers, 10):  # the enumerate() method adds counter to an iterable and returns it
    print ("i {0} has value {1}".format (i, n))

for i, n in enumerate (numbers):  # default index starts at zero
    print ("i {0} has value {1}".format (i, n))

for i, n in enumerate (numbers, 5):
    print ("i {0} has value {1}".format (i, n))
'''


def fpn(num):
    if num > 0:
        return num


num_list = range(-10, 10)
print(list(num_list))
positive_num_lst = list(filter(fpn, num_list))
print(positive_num_lst)


# user-defined function

def product_numbers(a, b):
    # this function returns the product of two numbers

    product = a * b
    return product


num1 = 30
num2 = 50
print ("product of {0} and {1} is {2}".format (num1, num2, product_numbers (num1, num2)))
