while True:
    def sum(a, b):
        return a + b


    def diff(a, b):
        return a - b


    def product(a, b):
        return a * b


    def division(a, b):
        return a / b


    print ('menu\n1.sum\n2.difference\n3.product\n4.division\n')
    ch = int (input ('Enter your choice'))
    n1 = float (input ('Enter a number'))
    n2 = float (input ('Enter a number'))
    if ch == 1:
        print ("The sum is: ", sum (n1, n2))
    elif ch == 2:
        print ("The difference is: ", diff (n1, n2))
    elif ch == 3:
        print ("The product is: ", product (n1, n2))
    elif ch == 4:
        if n2 == 0:
            print('Divide by zero')
        else:
            print ("The division is: ", division (n1, n2))
    else:
        print ('INVALID')