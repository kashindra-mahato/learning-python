import time
import threading


def cal_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square:", n*n)


def cal_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube:", n*n*n)


def cal_sum(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("sum:", n + n)


def cal_product(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("product:", n * n)


arr = [2, 3, 8, 9]

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))
t3 = threading.Thread(target=cal_sum, args=(arr,))
t4 = threading.Thread(target=cal_product, args=(arr,))

t1.start()
t2.start()
t3.start()
t4.start()

t = time.time()
cal_square(arr)
cal_cube(arr)
cal_sum(arr)
cal_product(arr)

t1.join()
t2.join()
t3.join()
t4.join()

print("time taken:", time.time() - t)

