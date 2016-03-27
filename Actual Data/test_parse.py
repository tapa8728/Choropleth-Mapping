from collections import defaultdict

#read files
user_data = open("gfg_users_states.csv", "r")
resp_data = open("gfg_personality_survey_responses.csv", "r")

f1 = open("user_dict.txt", "w")

lines_user = user_data.readlines()
lines_resp = resp_data.readlines()
m = []
k = []
d = {}			#create a dic
for l in lines_user:	#userid, states file
	m=l.split(",")	
	if m[1] != '\n':	#do nothing if state is null
		print m
		d[m[0]] = {'state' : m[1]}				# append an object to dictionary
		for l2 in lines_resp:	#userid, questionid, answer file
			k = l2.split(",")
			if(m[0] == k[0]):
				if m[0] in d:
						d[m[0]][k[1]]=k[2]	# if key found in d dictionary
	if(m[0] == '"15"'):
		break

p = d
f1.write(str(p))





