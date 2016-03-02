#read files
user_data = open("gfg_users_states.csv", "r")
resp_data = open("gfg_personality_survey_questions.csv", "r")

#write files
f1 = open("user_dict.txt", "w")

lines = user_data.readlines()

count = 0
full = 0
user = {}		#dict to store {gfgid : state} >> dont store if state is null
				#dict to store {gfgid : {q# : answer value ... (45 pairs)}}

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
f1.write(user)

print "Null States", count
print "Total records", full
print "Thus, usable records", (full-count)

k = resp_data.readlines()
for line in k:
	n = line.split(",")
	gfg_id = int(n[0].replace("\"", ""))
	while gfg_id in user.keys(): 
		anslist[n[1]] = n[2]

