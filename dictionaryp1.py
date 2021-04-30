kashindra = {'name': 'kashindra', 'assignment': [69, 70, 60], 'test': [90, 87, 88], 'lab' : [90, 70, 80]}
rajan = {'name': 'rajan', 'assignment': [69, 75, 68], 'test': [92, 80, 80], 'lab' : [93, 75, 84]}
sagun = {'name': 'sagun', 'assignment': [69, 70, 60], 'test': [70, 57, 80], 'lab' : [60, 75, 85]}
sooraj = {'name': 'sooraj', 'assignment': [69, 70, 60], 'test': [40, 87, 68], 'lab' : [60, 79, 80]}
students = [kashindra, rajan, sagun, sooraj]

for i in students:
    assign_total = i['assignment'][0] + i['assignment'][1] + i['assignment'][2]
    tst_total = i['test'][0] + i['test'][1] + i['test'][2]
    lab_total = i['lab'][0] + i['lab'][1] + i['lab'][2]
    score = (0.1 * (assign_total / 3)) + (0.7 * (tst_total / 3)) + (0.2 * (lab_total / 3))
    print(i['name'])
    if score >= 90:
        print('grage: A')

    elif score >= 80:
        print('grage: B')

    elif score >= 70:
        print('grage: C')

    elif score >= 60:
        print('grage: D')


