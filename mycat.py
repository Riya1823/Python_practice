import sys

'''try:
	file = None	
	file1=sys.argv[1]
	file = open(file1)

	i=0
	for line in file:
		print(i,line)
		i+=1
except IOError as err:
	print(err)
finally:
	if file is not None:
		file.close()'''

try:
	with open("/etc/passwd") as file:        #with will automatically close the file.
		i=1
		for line in file:
			print(i,line)
			i+=1
except IOError as err:
	print(err)

sys.exit()
