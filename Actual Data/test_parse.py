from collections import defaultdict

#read files
user_data = open("gfg_users_states.csv", "r")
resp_data = open("gfg_personality_survey_responses.csv", "r")

#write files
f1 = open("user_dict.txt", "w")
f2 = open("user_anser_dict", "w")
lines = user_data.readlines()

count = 0
full = 0
user = defaultdict(list)		#dict to store {gfgid : state} >> dont store if state is null
anslist ={}		#nested dict within user to store {gfgid : {q# : answer value ... (45 pairs)}}

for l in lines:
	full = full + 1
	m = l.split(",")
	if m[1] == '\n':
		count+=1	# dont add to user
	else:
		gfgid = int(m[0].replace("\"", ""))
		val = m[1].replace("\n", "").replace("\"", "")
		user[gfgid] = val 

#print "User dictionary ---", user 
dic = user
f1.write(str(dic))
print user[1]

print "Null States", count
print "Total records", full
print "Thus, usable records", (full-count)
a = []
k = resp_data.readlines()
for line in k:
	n = line.split(",")
	gfg_id = int(n[0].replace("\"", ""))
	if gfg_id in user.keys(): 	#(k,v) pair already present in dict, simple have to creeate a list and append to it. 
		a = [(n[1], n[2])]	
		user[gfg_id].append(a)
		a = [] #reset it

f2.write(str(user))
