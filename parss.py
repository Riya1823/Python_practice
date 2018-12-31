def hello(a,b,c=1,*args):
	print(a,b,c,args)

#hello(b=2,a=5,c=11,100,99)     #o/p:-5 2 1 ()      #5 2 11 ()     #error
hello(11,c=5,b=6)   #o/p:- 11 6 5 ()
