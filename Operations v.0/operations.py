import json
""" Operations on the personality data to convert it to a JSON file of format

	Required JSON Format- 
	{
		"NV": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "fillKey": "REP", "conscientiousness": "0", "gfgid": "1001", "openness": "38"}, 
		"CA": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "conscientiousness": "0", "gfgid": "2001", "openness": 56}, 
		"TX": {"extraversion": "0", "fillKey": "REP", "neuroticism": "0", "fillKey": "REP", "agreeableness": "0", "fillKey": "REP", "conscientiousness": "0", "fillKey": "REP"}
	}
	Converted data stored in data_1.json file in same folder
	"""
# Print Matrix
def display(m):
	print "Matrix is ------"
	for i in range(0,50):
		print statelist[i]," : ",m[i][0],",",m[i][1],",",m[i][2],",",m[i][3],",",m[i][4]

# Normalize the Matrix
def transform(m):
	o = [row[0] for row in m]
	o_norm = [float(i)*10/sum(o) for i in o]
	for i in range(0, 50):
		m[i][0] = o_norm[i]

	c = [row[1] for row in m]
	c_norm = [float(i)*10/sum(c) for i in c]
	for i in range(0, 50):
		m[i][1] = c_norm[i]

	e = [row[2] for row in m]
	e_norm = [float(i)*10/sum(e) for i in e]
	for i in range(0, 50):
		m[i][2] = e_norm[i]

	a = [row[3] for row in m]
	a_norm = [float(i)*10/sum(a) for i in a]
	for i in range(0, 50):
		m[i][3] = a_norm[i]

	n = [row[4] for row in m]
	n_norm = [float(i)*10/sum(n) for i in n]
	for i in range(0, 50):
		m[i][4] = n_norm[i]

# Function for getting Color
def color(v):
	if 0 <= v < 0.2:
		return 'LOW'
	elif 0.2 <= v < 0.4:
		return 'LOWMED'
	elif 0.4 <= v < 0.6:
		return 'MED'
	elif 0.6 <= v < 0.8:
		return 'HIGHMED'
	else:
		return 'HIGH'


# Function to format the data in required format
def dump_o(id_val, loc, a, orig):
	c = id_val-1;
	result = '"'+loc+'" : {"id": '+ str(id_val) +', "openness" : '+ str(orig[c][0])+',"fillKey" : "'+color(a[0])+'"}'
	return result

def dump_c(id_val, loc, a, orig):
	c = id_val-1;
	result = '"'+loc+'" : {"id": '+ str(id_val) +', "conscientiousness" : '+str(orig[c][1])+',"fillKey" : "'+color(a[1])+'"}'
	return result

def dump_e(id_val, loc, a, orig):
	c = id_val-1;
	result = '"'+loc+'" : {"id": '+ str(id_val) +', "extraversion": '+str(orig[c][2])+',"fillKey" : "'+color(a[2])+'"}'
	return result

def dump_a(id_val, loc, a, orig):
	c = id_val-1;
	result = '"'+loc+'" : {"id": '+ str(id_val) +', "agreeableness" : '+str(orig[c][3])+',"fillKey" : "'+color(a[3])+'"}'
	return result

def dump_n(id_val, loc, a, orig):
	c = id_val-1;
	result = '"'+loc+'" : {"id": '+ str(id_val) +', "neuroticism" : '+str(orig[c][4])+',"fillKey" : "'+color(a[4])+'"}'
	return result

# Raw data in comma-separated format
f = open("data.txt","r") 	#opens file with name of "data.txt"
fo = open("data_o.json", "w") #'w' mode will create a new file in the directory
fc = open("data_c.json", "w") 
fe = open("data_e.json", "w") 
fa = open("data_a.json", "w") 
fn = open("data_n.json", "w") 

lines = f.readlines()
statelist = [] # list of states in the same order
ocean_matrix =[[0 for x in range(5)] for x in range(50)]
orig =[[0 for x in range(5)] for x in range(50)] #duplicate matrix

count = 0 # to count the number of lines read from the file
# Step 1: Clean up data by removing spaces between each value
for l in lines:
	
	value=l.replace(" ","").replace("\n","").split(",")
	for i in range(2, 7):
		try:
			value[i] = int(value[i])	#Replace corrupt data of non-integer type to 0
		except:
			value[i] = 0;

	# Value 1 : GFGid
	# Value 2 : Location(State)
	# Values available for computation: 2,3,4,5,6
	# Step 2: Apply formula for Openness 7th position		
	tmp1=int(value[2])+int(value[3])+int(value[4])
	value[7] = tmp1
	ocean_matrix[count][0] = tmp1
	# Step 3: Apply formula for conscientiousness 8th position
	tmp2 = 2*int(value[2]) + int(value[3])
	value[8] = tmp2
	ocean_matrix[count][1] = tmp2
	# Step 4: Apply formula for extraversion 9th position	
	tmp3 = int(value[4])+int(value[5])+int(value[6])
	value[9] = tmp3
	ocean_matrix[count][2] = tmp3
	# Step 5: Apply formula for agreeableness 10th position	
	tmp4 = int(value[2])+int(value[4])+int(value[6])
	value[10] = tmp4
	ocean_matrix[count][3] = tmp4
	# Step 6: Apply formula for neuroticism	11th position
	tmp5 = 3*int(value[2]) + int(value[4])	
	value[11] = tmp5
	ocean_matrix[count][4] = tmp5
	# Step 7: Add to list of states	
	statelist.append(value[1])
	# Step 8: Increment the counter to add the next set of values to matrix
	count+=1 
	

print "StateList is-", statelist
display(ocean_matrix)

for i in range(0,50):
	for j in range(0,5):
		orig[i][j] = ocean_matrix[i][j]
# Step 9: Normalize the values in range of 0 to 1
transform(ocean_matrix)

display(ocean_matrix)

print "-------------------------- orig -------------------"
display(orig)

# Step 10: Convert matrix to JSON and dump for openness in data_o.json
counter = 0 # to access the state list
o_list = []
o_string = "{"
for row in ocean_matrix:
	state = statelist[counter]
	json_str_o = dump_o(counter+1, state, row, orig)	# Information string
	o_list.append(json_str_o) # Add it to a list
	counter+=1

o_string = str(o_list)	# Convert the list of information to a string
o_json = o_string.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", o_json
fo.write(o_json) # Final formatted string stored in data_1.json

# Step 11: Convert matrix to JSON and dump for openness in data_c.json
counter1 = 0 # to access the state list
c_list = []
c_string = "{"
for row in ocean_matrix:
	state = statelist[counter1]
	json_str_c = dump_c(counter1+1, state, row, orig)	# Information string
	c_list.append(json_str_c) # Add it to a list
	counter1+=1
c_string = str(c_list)	# Convert the list of information to a string
c_json =c_string.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", c_json
fc.write(c_json) # Final formatted string stored in data_1.json

# Step 12: Convert matrix to JSON and dump for openness in data_o.json
counter2 = 0 # to access the state list
e_list = []
e_string = "{"
for row in ocean_matrix:
	state = statelist[counter2]
	json_str_e = dump_e(counter2+1, state, row, orig)	# Information string
	e_list.append(json_str_e) # Add it to a list
	counter2+=1
e_string = str(e_list)	# Convert the list of information to a string
e_json = e_string.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", e_json
fe.write(e_json) # Final formatted string stored in data_1.json

# Step 13: Convert matrix to JSON and dump for openness in data_o.json
counter3 = 0 # to access the state list
a_list = []
a_string = "{"
for row in ocean_matrix:
	state = statelist[counter3]
	json_str_a = dump_a(counter3+1, state, row, orig)	# Information string
	a_list.append(json_str_a) # Add it to a list
	counter3+=1
a_string = str(a_list)	# Convert the list of information to a string
a_json = a_string.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", a_json
fa.write(a_json) # Final formatted string stored in data_1.json

# Step 10: Convert matrix to JSON and dump for openness in data_o.json
counter4 = 0 # to access the state list
n_list = []
n_string = "{"
for row in ocean_matrix:
	state = statelist[counter4]
	json_str_n = dump_n(counter4+1, state, row, orig)	# Information string
	n_list.append(json_str_n) # Add it to a list
	counter4+=1
n_string = str(n_list)	# Convert the list of information to a string
n_json = n_string.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", n_json
fn.write(n_json) # Final formatted string stored in data_1.json 

