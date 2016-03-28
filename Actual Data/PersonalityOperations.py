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
						if gfgid in self.userDict:
							#if key found in userDict dictionary
							self.userDict[gfgid][q_no]=str(ans)		
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
