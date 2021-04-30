def division(func):
    def function1():
        print("first")
        if int(b) == 0:
            print('cannot divide.')
            return func(a, b)
        return function1


def function2(a, b):
    return int(a)/int(b)

@division
function2(2, 2)



