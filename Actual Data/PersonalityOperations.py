import operator
import collections
import csv
import subprocess		#for executing R script from python file

#todo - 
# 1. O,C,E,A,N jsons in usJSON in proper format

class PersonalityOperations(object):
	'''
		Read 2 files Nested for loop to merge them into 1  
		Computation time ~ 11-12 mins 
	'''
	#super.__init__(self)

	def __init__(self):
		self.userData = None
		self.respData = None
		self.genAgeData = None
		self.userDict = {}	
		self.stateDict = {}		#state, OCEAN
		self.zStateDict ={}		#state, z-OCEAN 
		self.statewiseDict ={}  #state:[OCEAN]
		self.jsonString = None
		self.openString = None	#to build the openness.json
		self.amlist=[]
		userList = []
		respList= []
		
	'''
		Open and read "gfg_users_states.csv" & "gfg_personality_survey_responses.csv"
	'''	
	def readFile(self,fname1,fname2,fname3):
		self.userData = open(fname1, "r")	
		self.respData = open(fname2, "r")
		self.genAgeData = open(fname3, "r")
		print " >>>> End of readFile()"

	'''
		Create a new  file "user_dict.txt" that stores the nested dictionary with answers replaced with range (1 to 5)
		O,C,E,A,N values computed for each gfgid
	'''
	def writeFile(self,fname1,fname2,fname3,fname4,fname5):
		self.firstOutputFile = open(fname1, "w")
		self.secondOutputFile = open(fname2, "w")
		self.thirdOutputFile = open(fname3, "w")
		self.fourthOuputFile = open(fname4, "w")
		self.fifthOuputFile = open(fname5, "w")
		print " >>>> End of writeFile()"

	'''
		Read the files into respective lists
	'''
	def readintoList(self):
		self.userLines = self.userData.readlines()
		self.respLines = self.respData.readlines()
		self.genAgeLines = self.genAgeData.readlines()
		print " >>>> End of readintoList()"

	'''
		Close the opened files.
	'''
	def closeFile(self):
		userData.close()
		respData.close()
		genAgeData.close()
		print " >>>> End of closeFile()"

	'''
		Utility Function - R(Reverse Scoring) implemented to compute the O,C,E,A,N formulae
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
		# loop through states and gender,age files
		for uLine in self.userLines:								
			userList=uLine.split(",")
			#do nothing if state is null or DC or PR
			if userList[1] != '\n' :
				print "--> ", userList
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

			if( gfgid == "19"):
			 	break

		#Add gender,age data as well
		for l in self.genAgeLines:
			lis = l.split(",")
			#print "lis -------", lis
			gfgid, gen, age, state = lis[0], lis[1], lis[2], lis[3].replace("\n", "")
			if gfgid in self.userDict:
				if gen =="" or state == "" or age == "":	#weed out inconsistent values
					self.userDict[gfgid]['corrupt'] = 1 	#set that gfgid to corrupt as well coz no gender,age info wil be added for it 
				elif state == self.userDict[gfgid]['state']:	#if the state matches
					if gen == "male":
						self.userDict[gfgid]['gender'] = 0
					else:
						self.userDict[gfgid]['gender'] = 1
					#Replace the age of 99 with 80 (TBD)
					if age == str(99):
						self.userDict[gfgid]['age'] = str(80)	##replace 99 with 80
					else:
						self.userDict[gfgid]['age'] = age 
		#print "######### userDict", self.userDict
		print " >>>> End of combineUserDataAndResponses()"
	
	'''	
		Male=0, Female=1
		Create a new dictionary with only state and OCEAN values 
		{'gfgid':{'state': 'MI', 'gender':1/0, 'age':40, 'O':3, 'C':5, 'E':6, 'A':7, 'N':2'}}
	'''
	def relevantDict(self):
		for k in self.userDict:
			try:
				if self.userDict[k]['corrupt'] == 0 :	#only thse entires that are not corrupted
					if self.userDict[k]['gender']==0 or self.userDict[k]['gender']==1:
						self.stateDict[k] = {}
						self.stateDict[k]['state'] = self.userDict[k]['state']	
						self.stateDict[k]['gender']= self.userDict[k]['gender']
						self.stateDict[k]['age'] = self.userDict[k]['age']
						self.stateDict[k]['O'] = self.userDict[k]['O']
						self.stateDict[k]['C'] = self.userDict[k]['C']
						self.stateDict[k]['E'] = self.userDict[k]['E']
						self.stateDict[k]['A'] = self.userDict[k]['A']	
						self.stateDict[k]['N'] = self.userDict[k]['N']	
					else:
						pass
				else:
					pass
			except KeyError, e:	# Incase value(s) is missing for a "gfgid", delete it from the dictionary
			    print 'I got a KeyError - reason "%s"' % str(e)
			    self.userDict[k]['corrupt']	= 1
			except:
			    print 'I got another exception, but I should re-raise'
			    raise
		# print "StateDict is --------------- ", self.stateDict
		print " >>>> End of relevantDict()"

	'''
		Convert stateDict into a .csv file for R script to process
	'''
	def csvforR(self):
		# convert the stateDict.json file into a csv file - id, state, gender, age, O, C, E, A, N
		fout = open('stateDict.csv', 'wb')
		csvout = csv.writer(fout)
		csvout.writerow(["id"] +["state"] + ["gender"] + ["age"] + ["O"] + ["C"] +["E"] + ["A"]+ ["N"])
		for k, v in self.stateDict.iteritems():
			csvout.writerow([k] + [v['state']] + [v['gender']] + [v['age']] + [v['O']] +[v['C']] + [v['E']] +[v['A']] + [v['N']])
 		print " >>>> End of csvforR()"

	'''
		Call the linearReg.R script here
	'''
	def callRScript(self):
		# Define command and arguments
		command = 'Rscript'
		path2script = '/home/tanvip/Desktop/Choropleth-Mapping/Actual Data/linearReg.R'
		# Variable number of args in a list
		args = []
		# Build subprocess command
		cmd = [command, path2script] + args
		# check_output will run the command and store to result
		x = subprocess.check_output(cmd, universal_newlines=True)
		print('The value of x is -- ', x)
		print " >>>> End of callRScript()"

	'''
		Read the zscore.csv file and convert to dictionary
		O, C, E, A, N are the z-scored values
		zStateDict = {'gfgid':{'state': 'MI', 'O':3, 'C':5, 'E':6, 'A':7, 'N':2'}}
	'''
	def createZStateDict(self):
		zData = open("zscore.csv", "r")
		print "Successfully read zscore.csv"
		zLines = zData.readlines()
		for line in zLines[1:]:
			zList=line.split(",")
			#78, "OR" , 1,40, 3.2, 4.11, 2.38, 4.67, 1.88, -1.01592200338132,0.450660347883958,-0.965335669598581,1.56545378887604,-1.535226343548
			gfgid, state = zList[0], zList[1].replace("\"", "")
			z_o, z_c, z_e, z_a, z_n = zList[9], zList[10], zList[11], zList[12], zList[13].replace("\n", "")
			self.zStateDict[gfgid] = {}
			self.zStateDict[gfgid]['state'] = state
			self.zStateDict[gfgid]['O'] = round(float(z_o), 4)
			self.zStateDict[gfgid]['C'] = round(float(z_c), 4)
			self.zStateDict[gfgid]['E'] = round(float(z_e), 4)
			self.zStateDict[gfgid]['A'] = round(float(z_a), 4)
			self.zStateDict[gfgid]['N'] = round(float(z_n), 4)

		# print "zStateDict -----"
		# print self.zStateDict
		print " >>>> End of createZStateDict()"


	'''
		Create a new dictionary with statewise OCEAN values. Multiple values can be put into a list 
		{'state':{'O':[3], 'C':[5], 'E':[6], 'A':[7], 'N':[2]'}}

	'''
	def crunchStateDict(self):
		#self.statewiseDict={}
		list1=[]
		list2=[]
		list3=[]
		for each in self.zStateDict.values():
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

		# Compute average for each state
		for i,each in enumerate(self.statewiseDict.values()):
			for every in each.keys():
				each[every] = round((sum(each[every]) + 0.0) / len(each[every]), 4) if len(every)!=0 else 0
		
		print "StatewiseDict ----------------------------------------"	
		print self.statewiseDict
		print " >>>> End of crunchStateDict()"

	'''
		Set a flag "below" to 1 if a particular state has < 20 participants
		Append flag to the already crunched statewiseDict
	'''
	def flagState_20(self):
		test = self.stateDict
		state_count = {}	#dictonary that keep track of count of particpants belonging to a state
		for k,v in test.iteritems():
			st = v['state']
			#print "state - ", st
			if st not in state_count:
				state_count[st] = 1
			else:
				state_count[st] = state_count[st] + 1

		for k,v  in state_count.iteritems():
			print "State is ",k ," and value is-", v
			self.statewiseDict[k]['count'] = v

		for k,v in self.statewiseDict.iteritems():
			st = k
			if state_count[st] < 15:
				v['below'] = 1
			else:
				v['below'] = 0

		print "statewiseDict after adding below flag is ----"
		print self.statewiseDict
		print "End of flagState_20()"

	'''
		Convert to .json format for US MAP
	'''
	def usJSON(self):
		m = self.statewiseDict
		# add the color range
		scale_mean = 50
		scale_sd = 10
		low = 46
		lowmed = 48
		med = 50
		highmed = 52

		# Openness
		opendic={}
		for k,v in m.iteritems():
			opendic[k] = {}
			opendic[k]['openness'] = round((v['O']*scale_sd)+scale_mean, 4)
			if v['below'] == 1:
				opendic[k]['fillKey'] = 'X'
			else:
				if 0 <= opendic[k]['openness'] < low:
					opendic[k]['fillKey'] = 'LOW'
				elif low <= opendic[k]['openness'] < lowmed:
					opendic[k]['fillKey'] = 'LOWMED'
				elif lowmed <= opendic[k]['openness'] < med:
					opendic[k]['fillKey'] = 'MED'
				elif med <= opendic[k]['openness']< highmed:
					opendic[k]['fillKey']= 'HIGHMED'
				elif opendic[k]['openness'] >= highmed:
					opendic[k]['fillKey']= 'HIGH'

		self.openString = str(opendic).replace("'", "\"")
		print "Openness JSON -------------", self.openString
		file_o = open("open_data.json", "w")
		file_o.write(self.openString)

		# Concientiousness
		concdic={}
		for k,v in m.iteritems():
			concdic[k] = {}
			concdic[k]['conscientiousness'] = round((v['C']*scale_sd)+scale_mean, 4)
			if v['below'] == 1:
				concdic[k]['fillKey'] = 'X'
			else:
				if 0 <= concdic[k]['conscientiousness'] < low:
					concdic[k]['fillKey'] = 'LOW'
				elif low <= concdic[k]['conscientiousness'] < lowmed:
					concdic[k]['fillKey'] = 'LOWMED'
				elif lowmed <= concdic[k]['conscientiousness'] < med:
					concdic[k]['fillKey'] = 'MED'
				elif med <= concdic[k]['conscientiousness']< highmed:
					concdic[k]['fillKey']= 'HIGHMED'
				elif concdic[k]['conscientiousness'] >= highmed:
					concdic[k]['fillKey']= 'HIGH'

		cString = ""
		cString = str(concdic).replace("'", "\"")
		print "Conscientiousness JSON -------------", cString
		file_c = open("conc_data.json", "w")
		file_c.write(cString)

		# Extraversion
		extradic={}
		for k,v in m.iteritems():
			extradic[k] = {}
			extradic[k]['extraversion'] = round((v['E']*scale_sd)+scale_mean, 4)
			if v['below'] ==1:
				extradic[k]['fillKey'] = 'X'
			else:
				if 0 <= extradic[k]['extraversion'] < low:
					extradic[k]['fillKey'] = 'LOW'
				elif low <= extradic[k]['extraversion'] < lowmed:
					extradic[k]['fillKey'] = 'LOWMED'
				elif lowmed <= extradic[k]['extraversion'] < med:
					extradic[k]['fillKey'] = 'MED'
				elif med <= extradic[k]['extraversion']< highmed:
					extradic[k]['fillKey']= 'HIGHMED'
				elif extradic[k]['extraversion'] >= highmed:
					extradic[k]['fillKey']= 'HIGH'
		eString =""			
		eString = str(extradic).replace("'", "\"")
		print "extraversion JSON -------------", eString
		file_e = open("extra_data.json", "w")
		file_e.write(eString)

		# Agreeableness
		agreedic={}
		for k,v in m.iteritems():
			agreedic[k] = {}
			agreedic[k]['agreeableness'] = round((v['A']*scale_sd)+scale_mean, 4)
			if v['below'] ==1:
				agreedic[k]['fillKey'] = 'X'
			else:
				if 0 <= agreedic[k]['agreeableness'] < low:
					agreedic[k]['fillKey'] = 'LOW'
				elif low <= agreedic[k]['agreeableness'] < lowmed:
					agreedic[k]['fillKey'] = 'LOWMED'
				elif lowmed <= agreedic[k]['agreeableness'] < med:
					agreedic[k]['fillKey'] = 'MED'
				elif med <= agreedic[k]['agreeableness']< highmed:
					agreedic[k]['fillKey']= 'HIGHMED'
				elif agreedic[k]['agreeableness'] >= highmed:
					agreedic[k]['fillKey']= 'HIGH'
		aString =""			
		aString = str(agreedic).replace("'", "\"")
		print "agreeableness JSON -------------", aString
		file_a = open("agree_data.json", "w")
		file_a.write(aString)

		# Neuroticism
		neurodic={}
		for k,v in m.iteritems():
			neurodic[k] = {}
			neurodic[k]['neuroticism'] = round((v['N']*scale_sd)+scale_mean, 4)
			if v['below'] ==1:
				neurodic[k]['fillKey'] = 'X'
			else:
				if 0 <= neurodic[k]['neuroticism'] < low:
					neurodic[k]['fillKey'] = 'LOW'
				elif low <= neurodic[k]['neuroticism'] < lowmed:
					neurodic[k]['fillKey'] = 'LOWMED'
				elif lowmed <= neurodic[k]['neuroticism'] < med:
					neurodic[k]['fillKey'] = 'MED'
				elif med <= neurodic[k]['neuroticism']< highmed:
					neurodic[k]['fillKey']= 'HIGHMED'
				elif neurodic[k]['neuroticism'] >= highmed:
					neurodic[k]['fillKey']= 'HIGH'
		nString =""			
		nString = str(neurodic).replace("'", "\"")
		print "neuroticism JSON -------------", nString
		file_n = open("neuro_data.json", "w")
		file_n.write(nString)


		#convert the values to strings - no color information
		for each in m:
			for every in m[each]:
				s = str(m[each][every])
				m[each][every] = s

		self.jsonString = str(m).replace("'", "\"")


	'''
		Convert to .json format for AmCharts
	'''
	def amchartJSON(self):
		scale_mean = 50
		scale_sd = 10
		for each in self.statewiseDict:
			d2 = {}
			d2['state'] = each
			for every in self.statewiseDict[each]:
				d2['O'] = round((float(self.statewiseDict[each]['O'])*10) + 50, 4)
				d2['C'] = round((float(self.statewiseDict[each]['C'])*10) + 50, 4)
				d2['E'] = round((float(self.statewiseDict[each]['E'])*10) + 50, 4)
				d2['A'] = round((float(self.statewiseDict[each]['A'])*10) + 50, 4)
				d2['N'] = round((float(self.statewiseDict[each]['N'])*10) + 50, 4)
				
				
			self.amlist.append(d2)

		print "Amcharts JSON ------------- ", str(self.amlist).replace("'", "\"")
				

	'''
		Write userDict to the file "user_dict.txt"
	'''		
	def writeToFile(self):
		self.firstOutputFile.write(str(self.userDict))
		self.secondOutputFile.write(self.jsonString)
		self.thirdOutputFile.write(str(self.amlist).replace("'", "\""))
		self.fourthOuputFile.write(self.openString)
		self.fifthOuputFile.write(str(self.stateDict).replace("'", "\""))	#data for linear regression

	'''
		Utility Function - Weed out all the users with a set corrupt flag
	'''
	def cleanDict(self):
		cList = []
		for k in self.userDict:
			if self.userDict[k]['corrupt'] == 1:
				cList.append(k)
		#print "List of corrupt gfgid is - ", cList	

if __name__== "__main__":
	Po = PersonalityOperations()
	Po.readFile("gfg_users_states.csv","gfg_personality_survey_responses.csv", "gfg_users_gender_age_state.csv")
	Po.writeFile("user_dict.txt","final.json", "amcharts.json", "openness.json", "stateDict.json")
	Po.readintoList()
	Po.combineUserDataAndResponses()
	Po.relevantDict()
	Po.csvforR()
	Po.callRScript()
	Po.createZStateDict()
	# Po.cleanDict()
	Po.crunchStateDict()
	Po.flagState_20()
	Po.usJSON()			#FOR us map
	Po.amchartJSON()	#For Amcharts
	Po.writeToFile()
else:
	print "Wrong module imported."
