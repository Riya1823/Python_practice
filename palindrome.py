number = int(input("enter numbers:"))
string = str(input("enter string:"))
temp = number
rev = 0
while(number>0):
	dig = number%10
	rev = rev*10+dig
	number = number//10
if(temp == rev):
	print("The number is a palindrome!")                                         
else:
	print("the number is't palindrome!")

if string == string[::-1]:
    print("The string is palindrome!")
else:
    print("Not palindrome!")
