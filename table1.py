#def table(num, lines=10, symbol="x", spacing=0):
def table(num, lines=10, **kwargs):
	'''if "spacing" in kwargs:
		spacing = kwargs["spacing"]   
	else:
		spacing = 0  
	
	if "symbol" in kwargs:
		symbol = kwargs["symbol"]
	else:
		symbol = "x"    ''' 


	spacing = kwargs.get("spacing") or 0
	symbol = kwargs.get("symbol") or "x"

	for i in range(1,lines+1):
		print("{} {} {} = {}".format(num,symbol,i,num*i))

	for j in range(0,spacing +1):
		print()

def main():
	table(5,symbol="*")
	#table(5,spacing=3)


main()
