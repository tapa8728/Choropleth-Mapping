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
			m = self.userDict[gfgid]
			print "nested Dict --:   ", m
			for k in m:
				print "k is--", k, " and value is-", m[k]
			 	#print "key is - ", k, " and value is - ", v
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
