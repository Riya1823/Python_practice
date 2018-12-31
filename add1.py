def add(n1,n2,*args):		#*args will turn the both arguments into tuple or 
	res=0	
	res=n1+n2
	print(res)
	for val in args:
		res+=val
		print(res)	#return(res)

#add() #error
#add(11) #error
add(11,-1)
add(11,-1,-1)
