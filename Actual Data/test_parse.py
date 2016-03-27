from collections import defaultdict

#read files
user_data = open("gfg_users_states.csv", "r")
resp_data = open("gfg_personality_survey_responses.csv", "r")

lines_user = user_data.readlines()
lines_resp = resp_data.readlines()
m = []
k = []
d = {}			#create a dic
for l in lines_user:	#userid, states file
	m=l.split(",")	
	d[m[0]] = {'state' : m[1]}				# append an object to dictionary
	print m
	print d
	for l2 in lines_resp:	#userid, questionid, answer file
		k = l2.split(",")
		if(m[0] == k[0]):
			print k
	break





