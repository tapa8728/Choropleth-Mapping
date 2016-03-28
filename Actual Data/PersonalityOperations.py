class PersonalityOperations(object):
	'''
		Read 2 files Nested for loop to merge them into 1  Computation time ~ 11-12 mins 
	'''
	#super.__init__(self)

	def __init__(self):
		self.user_data = None
		self.resp_data = None
		self.d = {}	
		m = []
		k= []
		
	def readFile(self,fname1,fname2):
		self.user_data = open(fname1, "r")
		self.resp_data = open(fname2, "r")

	def writeFile(self,fname1):
		self.f1 = open(fname1, "w")

	def readintoList(self):
		self.lines_user = self.user_data.readlines()
		self.lines_resp = self.resp_data.readlines()

	def closeFile(self):
		user_data.close()
		resp_data.close()

	def computation(self):
		for l in self.lines_user:	#userid, states file
			m=l.split(",")	
			if m[1] != '\n':	#do nothing if state is null
				print m
				gfgid, state = m[0].replace("\"", ""), m[1].replace("\n", "").replace("\"", "")					
				self.d[gfgid] = {'state' : state}				# append an object to dictionary
				for l2 in self.lines_resp:	#userid, questionid, answer file
					k = l2.split(",")
					if(m[0] == k[0]):
						q_no, ans = k[1].replace("\"", ""), k[2].replace("\n", "").replace("\"", "")
						if gfgid in self.d:
							self.d[gfgid][q_no]=str(ans)	# if key found in d dictionary
			break
			
	def writeToFile(self):
		self.f1.write(str(self.d))

if __name__== "__main__":
	Po = PersonalityOperations()
	Po.readFile("gfg_users_states.csv","gfg_personality_survey_responses.csv")
	Po.writeFile("user_dict.txt")
	Po.readintoList()
	Po.computation()
	Po.writeToFile()
else:
	print "Wrong module imported."
