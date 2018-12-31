import sys
import os
z=input(sys.argv)
for root,dirs,files in os.walk('z'):
	for name in files:
		print(os.path.join(root,name))
	for name in dirs:
		print(os.path.join(root,name))
