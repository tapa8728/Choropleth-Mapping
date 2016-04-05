import operator
import collections
dic = {'1': {'state': 'MI', 'O': 2.33}, '2': {'state': 'MI', 'O': 5.7},  '3': {'state': 'CO', 'O': 6.1}, '4': {'state': 'CO', 'E': 9.1}}
#print dic.items(), len(dic.items())
dic2 = {'MI': { 'O': [2.33, 5.7] }, 'CO':{ 'O': [6.1], 'E' : [9.1] } }
ans={}
list1=[]
list2=[]
list3=[]
for each in dic.values():
	list1.append(each)
for each in list1:
	tmp=[]
	#print each.items()[0], each.items()[1]
	tmp.append(each.items()[0][1])
	tmp.append(each.items()[1][0])
	tmp.append(each.items()[1][1])
	list2.append(tmp)
	tmp=None
list3 = sorted(list2, key=operator.itemgetter(0, 1))
for i,each in enumerate(list3):
	if each[0] not in ans:		
		ans[each[0]] = {each[1]:[]}
	elif each[0] in ans:
		if (each[1] not in ans[each[0]]):
			ans[each[0]][each[1]]=[]
	ans[each[0]][each[1]].append(each[2])
print ans