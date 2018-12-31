import sys
string = str(input("Enter any String:"))

vovels = ('a','e','i','o','u')
for i in vovels:
    if i in string:
        print("Vovels present")
        sys.exit()     
    else:
        print("Vovel not present")
        sys.exit()
