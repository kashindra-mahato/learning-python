# from csv import reader
# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[2]}")
#
# from csv import reader
# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)
#
# from csv import DictReader
# with open("fighter.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row['Name'])


from csv import  writer, DictWriter
with open('cat.csv','w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Name", 1])

with open('cats.csv','w') as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({"Name": "Garfield",
                         "Breed": "Orange Tabby",
                         "Age":10})
    # n = input("Enter")
    #
    #     name = input("name:")
    #     breed = input("breed:")
    #     age = input("age:")
    #     csv_writer.writerow({"Name": name,
    #                          "Breed": breed,
    #                          "Age": age})
