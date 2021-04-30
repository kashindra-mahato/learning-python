import sys

lst = [2, 'b', 0]

for entry in lst:
    try:
        print("The entry is",entry)
        r = 1/entry

    #except TypeError:
        #print("This is Type error error.")


    except:
        print(sys.exc_info()[0])  # index [0:2]
        print("next entry")
        print("The reciprocal of ",entry, "is ",r )
    finally:
        print("finished")

    # raising errors manually

    # raise KeyboardInterrupt

try:
    num = int(input("Enter a number: "))
    if  num <= 0:
        raise ValueError("Error:entered negative number")
except ValueError as e:
    print(e)

try:
    f = open('sample.txt')
    # perform file operations
    f.close()
except IOError:
    print("Error:File not found")
except NameError:
    print("Error:Name Not found")

