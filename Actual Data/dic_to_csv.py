import csv

dic = {'10': {'A': 4.33, 'C': 4.89, 'E': 2.0, 'gender': 1, 'age': '40', 'O': 4.3, 'N': 4.0, 'state': 'MN'}, '27': {'A': 3.22, 'C': 3.22, 'E': 3.0, 'gender': 0, 'age': '30', 'O': 3.5, 'N': 2.88, 'state': 'MI'}, '15': {'A': 4.33, 'C': 3.22, 'E': 3.25, 'gender': 1, 'age': '70', 'O': 3.0, 'N': 1.5, 'state': 'AZ'}, '21': {'A': 4.22, 'C': 3.44, 'E': 1.5, 'gender': 1, 'age': '30', 'O': 3.2, 'N': 4.38, 'state': 'MI'}, '17': {'A': 4.0, 'C': 3.11, 'E': 2.5, 'gender': 0, 'age': '60', 'O': 3.4, 'N': 1.5, 'state': 'NJ'}, '19': {'A': 3.22, 'C': 2.67, 'E': 3.38, 'gender': 0, 'age': '40', 'O': 3.2, 'N': 3.25, 'state': 'NJ'}, '22': {'A': 4.11, 'C': 3.22, 'E': 2.38, 'gender': 0, 'age': '30', 'O': 4.3, 'N': 2.13, 'state': 'WA'}, '1': {'A': 3.78, 'C': 3.89, 'E': 2.75, 'gender': 0, 'age': '40', 'O': 3.6, 'N': 2.88, 'state': 'MI'}, '5': {'A': 3.44, 'C': 3.78, 'E': 2.25, 'gender': 0, 'age': '40', 'O': 3.8, 'N': 2.13, 'state': 'CO'}, '4': {'A': 4.11, 'C': 3.56, 'E': 3.88, 'gender': 0, 'age': '40', 'O': 4.1, 'N': 1.25, 'state': 'MI'}, '20': {'A': 3.78, 'C': 2.89, 'E': 3.13, 'gender': 1, 'age': '30', 'O': 4.6, 'N': 4.0, 'state': 'MN'}}


# convert the stateDict.json file into a csv file - id, state, gender, age, O, C, E, A, N
with open('stateDict.csv', 'wb') as fout:
    csvout = csv.writer(fout)
    for k, v in dic.iteritems():
    	#csvout.writerow( every['state'] + every['gender'] + int(every['age']) + every['O'] + every['C'] +every['E'] + every['A'] + every['N'])
        csvout.writerow([k] + [v['gender']])
     	# print "key is - ", k
     	# print "value is - ", v

