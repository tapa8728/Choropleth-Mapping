# test python script to try if an R script can be executed from python

import subprocess

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