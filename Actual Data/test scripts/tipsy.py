import operator
import collections
dic = {'10': {'A': 4.33, 'C': 4.89, 'E': 2.0, 'O': 4.3, 'N': 4.0, 'state': 'MN'}, '27': {'A': 3.22, 'C': 3.22, 'E': 3.0, 'O': 3.5, 'N': 2.88, 'state': 'MI'}, '15': {'A': 4.33, 'C': 3.22, 'E': 3.25, 'O': 3.0, 'N': 1.5, 'state': 'AZ'}, '21': {'A': 4.22, 'C': 3.44, 'E': 1.5, 'O': 3.2, 'N': 4.38, 'state': 'MI'}, '17': {'A': 4.0, 'C': 3.11, 'E': 2.5, 'O': 3.4, 'N': 1.5, 'state': 'NJ'}, '19': {'A': 3.22, 'C': 2.67, 'E': 3.38, 'O': 3.2, 'N': 3.25, 'state': 'NJ'}, '22': {'A': 4.11, 'C': 3.22, 'E': 2.38, 'O': 4.3, 'N': 2.13, 'state': 'WA'}, '1': {'A': 3.78, 'C': 3.89, 'E': 2.75, 'O': 3.6, 'N': 2.88, 'state': 'MI'}, '5': {'A': 3.44, 'C': 3.78, 'E': 2.25, 'O': 3.8, 'N': 2.13, 'state': 'CO'}, '4': {'A': 4.11, 'C': 3.56, 'E': 3.88, 'O': 4.1, 'N': 1.25, 'state': 'MI'}, '20': {'A': 3.78, 'C': 2.89, 'E': 3.13, 'O': 4.6, 'N': 4.0, 'state': 'MN'}}

#dic = {'1': { 'O': 2.33,'state': 'MI'}, '2': {'state': 'MI', 'O': 5.7},  '3': {'state': 'CO', 'C': 6.1}, '4': {'state': 'CO', 'E': 9.1}, '5': {'state': 'UT', 'E': 9.1}}



#print dic.items(), len(dic.items())
dic2 = {'MI': { 'O': [2.33, 5.7] }, 'CO':{ 'O': [6.1], 'E' : [9.1] } }
ans={}
list1=[]
list2=[]
list3=[]
for each in dic.values():
	list1.append(each)

'''
for each in list1:
	print each
exit()
'''
for each in list1:
	tmp=[]
	tmp.append(each['state'])
	tmp.append(each['O'])
	tmp.append(each['C'])
	tmp.append(each['E'])
	tmp.append(each['A'])
	tmp.append(each['N'])
	list2.append(tmp)
	tmp=None
'''
for each in list2:
	print each
exit()
'''

list3 = sorted(list2, key=operator.itemgetter(0, 1))
#list3 = sorted(list2, key=list[0])
'''
for each in list3:
	print each
exit()
'''


'''
for i,each in enumerate(list3):
	if each[0] not in ans:		
		ans[each[0]] = {each[1]:[]}
	elif each[0] in ans:
		if (each[1] not in ans[each[0]]):
			ans[each[0]][each[1]]=[]
	ans[each[0]][each[1]].append(each[2])
print ans
'''

for i,each in enumerate(list3):
	if each[0] not in ans:
		ans[each[0]] = {'O':[],'C':[],'E':[],'A':[],'N':[]}		
		ans[each[0]]['O'].append(each[1])
		ans[each[0]]['C'].append(each[2])
		ans[each[0]]['E'].append(each[3])
		ans[each[0]]['A'].append(each[4])
		ans[each[0]]['N'].append(each[5])


	elif each[0] in ans:
		#print ans[each[0]]['A']
		#exit()
		ans[each[0]]['O'].append(each[1])
		ans[each[0]]['C'].append(each[2])
		ans[each[0]]['E'].append(each[3])
		ans[each[0]]['A'].append(each[4])
		ans[each[0]]['N'].append(each[5])

ans_avg={}
'''
for i,each in enumerate(ans.values()):
	print each
	#print ans.keys()
	for every in each.keys():
		#print every
		#print each[every]
		each[every] = (sum(each[every]) + 0.0 / len(each[every])) if len(every)!=0 else 0
	raw_input()
'''



d = {'a':{ 'b':20,'c':30} }

'''
for each in (d.values()):
	print each
	for every in each.keys():
		each[every]= 100
print d
'''
ds = [1,2,3,[4,5,6]]
for i,each in enumerate(ds):
	each[3] = 100
print ds

