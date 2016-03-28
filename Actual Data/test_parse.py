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
		gfgid = m[0].replace("\"", "")					#can be put into a function int_cleanup()
		state = m[1].replace("\n", "").replace("\"", "")	#can be put into a function string_cleanup()
		d[gfgid] = {'state' : state}				# append an object to dictionary
		print "gfgid:",gfgid," state:",state
		for l2 in lines_resp:	#userid, questionid, answer file
			k = l2.split(",")
			if(m[0] == k[0]):
				q_no = k[1].replace("\"", "")
				ans = k[2].replace("\n", "").replace("\"", "")
				if gfgid in d:
					d[gfgid][q_no]=str(ans)	# if key found in d dictionary
	
print d
p = d
f1.write(str(p))





