while True:
    def time_con():
        a = input("Enter time in 12 hours format: ")
        if 0 < int(a[:2]) <= 12 and 0 < int(a[3:5]) < 60 and 0 < int(a[6:8]) < 60:
            if a[8:10] == "pm":
                if int (a[:2]) < 12:
                    b = int (a[:2]) + 12
                    print ("The time in 24 hour format is {}:{}:{}".format (str (b), a[3:5], a[6:8]))
                else:
                    print ("The time in 24 hour format is {}:{}:{}".format (a[:2], a[3:5], a[6:8]))
            elif a[8:10] == "am":
                if int (a[:2]) == 12:
                    print ("The time in 24 hour format is {}:{}:{}".format ("00", a[3:5], a[6:8]))
                else:
                    print ("The time in 24 hour format is {}:{}:{}".format (a[:2], a[3:5], a[6:8]))
        else:
            print("Enter a valid time i.e, 0<hr<=12, 0<min<60 and 0<second<60 example format: 01:43:54pm")
    time_con()
