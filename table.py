
def table(num1,num2,sym):
	if num1 <= 0 or num2 <= 0:
		raise Exception("Error:no -ve or 0 values.")
	for i in range(1,num2+1):
		mul = 1
		mul = num1*i
		print(num1,sym,i,"=",mul)
	return table
try:
	num1 = int(input("enter numbers for table:\n"))
	num2 = int(input("upto which no mul:\n"))
	sym = str(input("Enter a Character:\n"))
	table(num1,num2,sym)
except Exception as e:
	print(e)


