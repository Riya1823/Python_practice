import sys
count=111
obj={
	"fname":"Riya",
	"lname":"Gupta",
	"city":"pune"
     }
record[count]=obj

while True:
	choice = int(input("Enter 1)Add\n 2)Show\n"))
	if choice==1:
		prn=int(input("prn"))
		fname=input("First Name:")
		lname=input("Last Name:")
		city=input("City:")
		
		if prn in obj:
		print("not found")
		continue

		obj[prn] = {"fname": fname,"lname": lname, "city": city}
		print("Record sucessful")



	elif choice== "2":
		prn = int(input(""))
		

		data = obj[prn]
		print("\n")
		print("prn: {}".format(prn))
		print("fname: {}".format(prn))
		print("lname: {}".format(prn))
		print("city: {}".format(data["city"]))
		
	elif choice == "3":
		try:
			prn = int(input("Enter PRN:"))
		except ValueError as e:
			print(e)
			continue

		if prn not in obj:
			print("Error:student with roll no{} doesn't exit\n".format(prn))
			continue

		field_to_update = input("What field you want to update?(valid choices: fname,lname,city):")
		if field_to_update not in ("fname","lname","city"):
			print("\nError:fiels '{}' doesn't exit\n".format(field_to_update))

 

	elif choice == "4":
		try:						#excetion handling.
			prn =int(input("Enter PRN:"))
			del obj[prn]
			print("\nRecord Sucessfully deleted\n")
		except ValueError as err:
			print(err)
			continue
		except KeyError as err
			print("\nError:student with prn{} doesn't exit\n".format(prn))
		#print("Sucessful")


	elif choice =="5":
		for prn,data in obj.items():
			print("\n")
			print("PRN	  :{}".format(prn))
			print("First Name :{}".format(data["fname"]))
			print("Last Name  :{}".format(data["lname"]))
			print("City	  :{}".format(data["city"))
		record[count]=obj
	sys.exit()
