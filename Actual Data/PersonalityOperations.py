import operator
import collections
import numpy

class PersonalityOperations(object):
	'''
		Read 2 files Nested for loop to merge them into 1  
		Computation time ~ 11-12 mins 
	'''
	#super.__init__(self)

	def __init__(self):
		self.userData = None
		self.respData = None
		self.userDict = {}	
		self.stateDict = {}		#state, OCEAN
		self.statewiseDict ={}  #state:[OCEAN]
		self.jsonString = None
		self.amlist=[]
		userList = []
		respList= []
		
	'''
		Open and read "gfg_users_states.csv" & "gfg_personality_survey_responses.csv"
	'''	
	def readFile(self,fname1,fname2):
		self.userData = open(fname1, "r")	
		self.respData = open(fname2, "r")

	'''
		Create a new  file "user_dict.txt" that stores the nested dictionary with answers replaced with range (1 to 5)
		O,C,E,A,N values computed for each gfgid
	'''
	def writeFile(self,fname1,fname2,fname3):
		self.firstOutputFile = open(fname1, "w")
		self.secondOutputFile = open(fname2, "w")
		self.thirdOutputFile = open(fname3, "w")

	'''
		Read the files into respective lists
	'''
	def readintoList(self):
		self.userLines = self.userData.readlines()
		self.respLines = self.respData.readlines()

	'''
		Close the opened files.
	'''
	def closeFile(self):
		userData.close()
		respData.close()

	'''
		Function R(Reverse Scoring) implemented to compute the O,C,E,A,N formulae
	'''
	def reverse(self,n):
		rev = 0
		if n == 1:
			rev = 5
		elif n == 2:
			rev = 4
		elif n == 3:
			rev = 3
		elif n == 4:
			rev = 2
		elif n == 5:
			rev = 1
		return rev

	'''
		Read from lists, clean-up code and merge into a nested dictionary (userDict)
		userDict(key) is gfgid 
		userDict(value) is a another dict ..
			-keys = question#[1-45], state, O, C, E, A, N
			-value = answers[1-45], "state", Ans(O), Ans(C), Ans(E), Ans(A), Ans(N) 
		
	''' 
	def combineUserDataAndResponses(self):
		#userid, states file
		count=0
		for uLine in self.userLines:								
			userList=uLine.split(",")
			#do nothing if state is null or DC or PR
			if userList[1] != '\n':
				print userList
				gfgid, state = userList[0].replace("\"", ""), userList[1].replace("\n", "").replace("\"", "")	
				if state!= 'PR' or state!='DC':

					self.userDict[gfgid] = {'state' : state}				# append an object to dictionary
					#userid, questionid, answer file
					for rLine in self.respLines:						
						respList = rLine.split(",")
						if(userList[0] == respList[0]):
							q_no, ans = respList[1].replace("\"", ""), respList[2].replace("\n", "").replace("\"", "")
							if ans == 'Disagree strongly':
								ans = 1
							elif ans == 'Disagree a little':
								ans = 2
							elif ans == 'Neither agree':	#neutrals
								ans = 3
							elif ans == 'Agree a little':
								ans = 4
							elif ans == 'Agree strongly':
								ans = 5
							else:	# question#45 is feedback and does not need to be replaced
								ans = str(ans)
							#print "After conversion  --> ",q_no," --", ans
							if gfgid in self.userDict:
								#if key found in userDict dictionary
								self.userDict[gfgid][q_no]=ans
			# Calculate O,C,E,A,N values after this point and add those (key,value) pairs to the nested dictionary
			# Only then move to the next user
			try:
				nD = self.userDict[gfgid]
				self.userDict[gfgid]['corrupt'] = 0		# initially set the corrupt flag to false
				# Openness = 5, 10, 15, 20, 25, 30, 35R, 40, 41R, 44
				self.userDict[gfgid]['O'] = round(float(nD['5'] + nD['10'] + nD['15'] + nD['20']+ nD['25'] + nD['30'] 
				+ self.reverse(nD['35']) + nD['40'] + self.reverse(nD['41']) + nD['44'])/10, 2)

				# Conscientiousness: 3, 8R, 13, 18R, 23R, 28, 33, 38, 43R
				self.userDict[gfgid]['C'] = round(float(int(nD['3']) + self.reverse(int(nD['8'])) + int(nD['13']) + self.reverse(int(nD['18'])) 
				+ self.reverse(int(nD['23'])) + int(nD['28']) + int(nD['33']) + int(nD['38']) + self.reverse(int(nD['43'])))/9, 2)

				# Extraversion: 1, 6R, 11, 16, 21R, 26, 31R, 36
				self.userDict[gfgid]['E'] = round(float(int(nD['1']) + self.reverse(int(nD['6'])) + int(nD['11']) + int(nD['16']) 
				+ self.reverse(int(nD['21'])) + int(nD['26']) + self.reverse(int(nD['31'])) + int(nD['36']))/8, 2)

				# Agreeableness: 2R, 7, 12R, 17, 22, 27R, 32, 37R, 42
				self.userDict[gfgid]['A'] = round(float(self.reverse(int(nD['2'])) + int(nD['7']) + self.reverse(int(nD['12'])) + int(nD['17'])+ int(nD['22'])  
				+ self.reverse(int(nD['27'])) + int(nD['32']) + self.reverse(int(nD['37'])) + int(nD['42']))/9, 2)

				# Neuroticism: 4, 9R, 14, 19, 24R, 29, 34R, 39
				self.userDict[gfgid]['N'] = round(float(int(nD['4']) + self.reverse(int(nD['9'])) + int(nD['14']) + int(nD['19'])+ self.reverse(int(nD['24'])) 
					+ int(nD['29']) + self.reverse(int(nD['34'])) + int(nD['39']))/8, 2) 

			except KeyError, e:	# Incase value(s) is missing for a "gfgid", delete it from the dictionary
			    print 'I got a KeyError - reason "%s"' % str(e)
			    self.userDict[gfgid]['corrupt']	= 1
			except:
			    print 'I got another exception, but I should re-raise'
			    raise

			# print ""
			# print "######### ", self.userDict
			# if( gfgid == "27"):
			#  	break
		

	'''
		Weed out all the users with a set corrupt flag
	'''
	def cleanDict(self):
		cList = []
		for k in self.userDict:
			if self.userDict[k]['corrupt'] == 1:
				cList.append(k)
				
		print "List of corrupt gfgid is - ", cList	

	'''
		Create a new dictionary with only state and OCEAN values 
		{'gfgid':{'state: 'MI', 'O':3, 'C':5, 'E':6, 'A':7, 'N':2'}}
	'''
	def relevantDict(self):
		for k in self.userDict:
			if self.userDict[k]['corrupt'] == 0:	#only thse entires that are not corrupted
				self.stateDict[k] = {}
				self.stateDict[k]['state'] = self.userDict[k]['state']	
				self.stateDict[k]['O'] = self.userDict[k]['O']
				self.stateDict[k]['C'] = self.userDict[k]['C']
				self.stateDict[k]['E'] = self.userDict[k]['E']
				self.stateDict[k]['A'] = self.userDict[k]['A']	
				self.stateDict[k]['N'] = self.userDict[k]['N']	

		print "State dictionary is - ", self.stateDict

	'''
		Create a new dictionary with statewise OCEAN values. Multiple values can be put into a list 
		{'state':{'O':[3], 'C':[5], 'E':[6], 'A':[7], 'N':[2]'}}

	'''
	def crunchStateDict(self):
		#self.statewiseDict={}
		list1=[]
		list2=[]
		list3=[]
		for each in self.stateDict.values():
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
		for i,each in enumerate(list3):
			if each[0] not in self.statewiseDict:
				self.statewiseDict[each[0]] = {'O':[],'C':[],'E':[],'A':[],'N':[]}		
				self.statewiseDict[each[0]]['O'].append(each[1])
				self.statewiseDict[each[0]]['C'].append(each[2])
				self.statewiseDict[each[0]]['E'].append(each[3])
				self.statewiseDict[each[0]]['A'].append(each[4])
				self.statewiseDict[each[0]]['N'].append(each[5])
			elif each[0] in self.statewiseDict:
				#print ans[each[0]]['A']
				#exit()
				self.statewiseDict[each[0]]['O'].append(each[1])
				self.statewiseDict[each[0]]['C'].append(each[2])
				self.statewiseDict[each[0]]['E'].append(each[3])
				self.statewiseDict[each[0]]['A'].append(each[4])
				self.statewiseDict[each[0]]['N'].append(each[5])

		# Compute avergage for each state
		for i,each in enumerate(self.statewiseDict.values()):
			for every in each.keys():
				each[every] = round((sum(each[every]) + 0.0 / len(each[every])), 2) if len(every)!=0 else 0
		
		print "----------------------------------------"	
		print self.statewiseDict

	'''
		Convert to .json format for US MAP
	'''
	def jsonConvert1(self):
		m = self.statewiseDict
		for each in m:
			for every in m[each]:
				s = str(m[each][every])
				m[each][every] = s

		self.jsonString = str(m).replace("'", "\"")


	'''
		Convert to .json format for amcharts
	'''
	def jsonConvert2(self):
		for each in self.statewiseDict:
			d2 = {}
			d2['state'] = each
			for every in self.statewiseDict[each]:
				d2['O'] = self.statewiseDict[each]['O']
				d2['C'] = self.statewiseDict[each]['C']
				d2['E'] = self.statewiseDict[each]['E']
				d2['A'] = self.statewiseDict[each]['A']
				d2['N'] = self.statewiseDict[each]['N']
			self.amlist.append(d2)

		print "AMLISt is - ", str(self.amlist).replace("'", "\"")
				

	'''
		Write userDict to the file "user_dict.txt"
	'''		
	def writeToFile(self):
		self.firstOutputFile.write(str(self.userDict))
		self.secondOutputFile.write(self.jsonString)
		self.thirdOutputFile.write(str(self.amlist).replace("'", "\""))


if __name__== "__main__":
	Po = PersonalityOperations()
	Po.readFile("gfg_users_states.csv","gfg_personality_survey_responses.csv")
	Po.writeFile("user_dict.txt", "final.json", "amcharts.json")
	Po.readintoList()
	Po.combineUserDataAndResponses()
	Po.relevantDict()
	Po.cleanDict()
	Po.crunchStateDict()
	Po.jsonConvert1()	#FOR us map
	Po.jsonConvert2()	#For Amcharts
	Po.writeToFile()
else:
	print "Wrong module imported."
