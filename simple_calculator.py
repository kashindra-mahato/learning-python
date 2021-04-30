while True:
    li = []
    n = int(input("Enter iteration times for number input:"))
    for x in range(0,n):
        li.append(int(input("Enter a number ")))
    op = input("operator")

    if(op == '+'):
        print('The sum is: ',(li[0]+li[1]))
    elif(op == '-'):
        print('difference is: ',(li[0]-li[1]))
    elif(op == '/'):
        if(li[1] == 0):
            print('divided by zero')
        else:
            print('division is: ',(li[0]/li[1]))
    elif(op == '*'):
        print('product is: ',(li[0]*li[1]))
    else:
        break


