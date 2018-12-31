import sys
try:
	with open("/etc/passwd") as file:        #with will automatically close the file.
		i=1
		while(i<4):
			for line in file:
				print(line)
				i+=1
except IOError as err:
	print(err)

sys.exit()
