

def factorial(num=5):
	if num < 0:
		raise Exception("We do not accept -ve values")
	NO = 1
	for i in range(1,num+1):
		NO = NO*i
		print("factorial of",num,"is =",NO)
	return factorial  				#if the function is not returining it will return null by default


try:
	res = factorial()
	#res = factorial(num =5)
	#res = factorial(num = int(input("enter numbers:")))
	print(res)
except Exception as e:
	print(e)
#print("factorial of",num,"is =",NO)
    



