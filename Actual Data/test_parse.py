f = open("gfg_users_states.csv", "r")
lines = f.readlines()

count = 0
full = 0

for l in lines:
	full = full + 1
	m = l.split(",")
	if m[1] == '\n':
		count+=1

print "Number of records with null values", count
print "Number of records in total", full
print "Thus, number of records usable", (full-count)
