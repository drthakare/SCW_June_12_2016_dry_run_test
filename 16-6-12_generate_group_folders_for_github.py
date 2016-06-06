'''
Authors: 

This is a scrip that makes two plots
'''
import os

for i in range(25):
	directory = 'group_'+str(i+1)+'/'
	if not os.path.exists(directory):
		os.makedirs(directory)
		readme = file(directory + 'readme.rm','w')
		readme.close()


