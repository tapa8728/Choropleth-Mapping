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
	def writeFile(self,fname1):
		self.firstOutputFile = open(fname1, "w")

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
			#do nothing if state is null
			if userList[1] != '\n':	
				print userList
				gfgid, state = userList[0].replace("\"", ""), userList[1].replace("\n", "").replace("\"", "")					
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
						elif ans == 'Neither agree':	#neutral
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
							self.userDict[gfgid][q_no]=str(ans)		
			# Calculate O,C,E,A,N values after this point and add those (key,value) pairs to the nested dictionary
			# Only then move to the next user
			print "dict ---> ", self.userDict
			nD = self.userDict[gfgid]
			print ""
			print "nested Dict -- :   ", nD
			# Openness = 5, 10, 15, 20, 25, 30, 35R, 40, 41R, 44
			openVal = int(nD['5']) + int(nD['10']) + int(nD['15']) + int(nD['20'])+ int(nD['25']) + int(nD['30']) + int(nD['35']) + int(nD['40']) + int(nD['41']) + int(nD['44'])
			print "Reverse of 10 --", self.reverse(int(nD['10'])), " and nD['10'] is ", nD['10']
			print "Openness -- ", openVal
			# Conscientiousness: 3, 8R, 13, 18R, 23R, 28, 33, 38, 43R
			concVal =4
			# Extraversion: 1, 6R, 11, 16, 21R, 26, 31R, 36
			extraVal =4
			# Agreeableness: 2R, 7, 12R, 17, 22, 27R, 32, 37R, 42
			agreeVal =4
			# Neuroticism: 4, 9R, 14, 19, 24R, 29, 34R, 39
			neuroVal = 4
			break
	
	'''
		Write userDict to the file "user_dict.txt"
	'''		
	def writeToFile(self):
		self.firstOutputFile.write(str(self.userDict))


if __name__== "__main__":
	Po = PersonalityOperations()
	Po.readFile("gfg_users_states.csv","gfg_personality_survey_responses.csv")
	Po.writeFile("user_dict.txt")
	Po.readintoList()
	Po.combineUserDataAndResponses()
	Po.writeToFile()
else:
	print "Wrong module imported."
