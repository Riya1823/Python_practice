students = {}

while True:
    print("-------------MENU-------------")
    print("1. Add student data")
    print("2. Show student data")
    print("3. Update student data")
    print("4. Delete student data")
    print("5. Show all students")
    print("6. Exit")

    choice = input("Enter your choice: ")




    if choice == "1":
        rollno = int(input("Enter Roll No.: "))
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        city = input("Enter city: ")

        if rollno in students:
            print("\nERROR: student with roll no {} already exist\n".format(rollno))
            continue

        students[rollno] = {"fname": fname, "lname": lname, "city": city}
        print("\nRecord successfully added\n")




    elif choice == "2":
        rollno = int(input("Enter Roll No.: "))

        if rollno not in students:
            print("\nERROR: student with roll no {} doesn't exist\n".format(rollno))
            continue

        data = students[rollno]
        print("\n")
        print("ROLL NO.   : {}".format(rollno))
        print("FIRST NAME : {}".format(data["fname"]))
        print("LAST NAME  : {}".format(data["lname"]))
        print("CITY       : {}".format(data["city"]))
        print("\n")




    elif choice == "3":
        try:
            rollno = int(input("Enter Roll No.: "))
        except ValueError as e:
            print(e)
            continue

        if rollno not in students:
            print("\nERROR: student with roll no {} doesn't exist\n".format(rollno))
            continue

        field_to_update = input("What field you want to update? (Valid choices: fname, lname, city): ")
        if field_to_update not in ("fname", "lname", "city"):
            print("\nERROR: field '{}' doesn't exist\n".format(field_to_update))
            continue

        new_value = input("Enter new value for field '{}': ".format(field_to_update))
        students[rollno][field_to_update] = new_value
        print("\nRecord successfully updated\n")




    elif choice == "4":
        try:
            rollno = int(input("Enter Roll No.: "))
            del students[rollno]
            print("\nRecord successfully deleted\n")
        except ValueError as err:
            print(err)
        except KeyError as err:
            print("\nERROR: student with roll no {} doesn't exist\n".format(rollno))




    elif choice == "5":
        for rollno, data in students.items():
            print("\n")
            print("ROLL NO.   : {}".format(rollno))
            print("FIRST NAME : {}".format(data["fname"]))
            print("LAST NAME  : {}".format(data["lname"]))
            print("CITY       : {}".format(data["city"]))
            print("\n")




    elif choice == "6":
        break
    else:
        print("\nWrong choice :(\n")
