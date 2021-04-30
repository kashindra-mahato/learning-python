# day1
'''# dict1 = {key1:value1, key2:value2, key3:value3}
# dict2 = dict([(key1,value1), (key2,value2), (key3,value3)])
# dict3 = dict({     })
# we can define list, tuple, set in dictionary

dict1 = {1: "hari", 2: "shyam", 3: "gopal"}
print(dict1)
dict2 = dict([("key1", "hari"), (2, "shyam"), (3, "ram")])
print(dict2)
dict3 = dict({1: "hari", 2: "shyam", 3: "gopal"})
print(dict3)

# nested dictionary
dict4 = {1: 'hari', 2: 'hero', 3: {'A': 'Alpha', 'B': 'Beta', 'c': (1, 2, 3)}}
print(dict4)
print(dict4[3]['c'])
dict5 = {(1, 2, 3): ['rajan', 4, 7], 2: (2, 3, 5), 3: [4, 3, 7], 4: {1: 'rajan', 2: (2, [3, 5], 5), 3: [4, 3, 7]}}
print(dict5)
print(dict5[4][3][1])
print(dict5[(1, 2, 3)][0])
dict6 = {1: 'hari', 2: 'hero', 3: {'A': 'Alpha', 'B': 'Beta', 'c': (1, 2, 3)}}

"""
dict5 = {(1, 2, 3): ['rajan', 4, 7], 2: (2, 3, 5), 3: [4, 3, 7], 4: {1: 'rajan', 2: (2, [3, 5], 5), [2, 4]: [4, (3, 4), 7]}}
print(dict5) # list cannot be set as key

dict5 = {(1, 2, 3): ['rajan', 4, 7], 2: (2, 3, 5), 3: [4, 3, 7], 4: {1: 'rajan', {3, 5}: (2, [3, 5], 5), 3: [4, (3, 4), 7]}}
print(dict5)  # set cannot be set as key

"""

dict5[2] = 3
print(dict5)

# dict5[4][2][1] = 5
# tupple object cannot be defined
# print(dict5)

apple = {}
apple[0] = 1
print(apple)
apple[1] = 3
print(apple)
apple[1]['a'] = {}
# nested cannot be created or may be...ghar gayera herni
print(apple)

dict7 = {1: 'hari', 2: 'hero', 3: {'A': 'Alpha', 'B': 'Beta', 'c': (1, 2, 3)}}
dict7[3]['B'] = 'beta2'
print(dict7)

'''

# day2

dict_a = {1: 'hari', 2: 'hero', 3: {'A': 'Alpha', 'B': 'Beta', 'c': (1, 2, 3)}}
print(dict_a.get(3)['B'])  # accessing element using get() function
print(dict_a.get(3)['c'][1])

# del dict_a[2]  # deleting a specific key
# print('\ndeleting a specific key: ')
# print(dict_a)

del dict_a[3]['B']
print('\ndeleting a nested key: ')
print(dict_a)

dict_a.pop(1)
print(dict_a)

dict_a.popitem()  # delete last element
print(dict_a)

dict_b = {1: 'hari', 2: 'hero', 3: {'A': 'Alpha', 'B': 'Beta', 'c': (1, 2, 3)}}
# dict_b.clear()  # deletes all elements from dictionary
print(dict_b)
print(len(dict_b))

dict_b.update({1: 'rajan'})  # updating
print(dict_b)
print(dict_b.keys())
print(dict_b.values())
print(dict_b.items())
print(dict_b.popitem())
# dict_b.fromkeys()  # ghar ma gayera herne
x = (1, 2, 3)
y = 0
z = dict.fromkeys(x,y)
print(z)