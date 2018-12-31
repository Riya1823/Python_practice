
# CREATE OPERATION
def add_student(database, rollno, fname, lname, city):
    if rollno in database:
        raise Exception("\nERROR: student with roll no {} already exists\n".format(rollno))

    database[rollno] = {"fname": fname, "lname": lname, "city": city}


# HELPER FUNCTION
def _print_student_data(rollno, data):
    print("\n")
    print("ROLL NO.   : {}".format(rollno))
    print("FIRST NAME : {}".format(data["fname"]))
    print("LAST NAME  : {}".format(data["lname"]))
    print("CITY       : {}".format(data["city"]))
    print("\n")


# READ OPERATION
def show_student(database, rollno):
    if rollno not in database:
        raise Exception("\nERROR: student with roll no {} doesn't exist\n".format(rollno))
    
    data = database[rollno]
    _print_student_data(rollno, data)         #calling of func


# READ OPERATION
def show_all_students(database):
    for rollno, data in database.items():
        _print_student_data(rollno, data)


# UPDATE OPERATION
def update_student(database, rollno, field_to_update, new_value):
    if rollno not in database:
        raise Exception("\nERROR: student with roll no {} doesn't exist\n".format(rollno))

    if field_to_update not in ("fname", "lname", "city"):
        raise Exception("\nERROR: '{}' is invalid field for a student\n".format(field_to_update))

    database[rollno][field_to_update] = new_value


# DELETE OPERATION
def delete_student(database, rollno):
    if rollno not in database:
        raise Exception("\nERROR: student with roll no {} doesn't exist\n".format(rollno))

    del database[rollno]


def main():
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
            try:
                rollno = int(input("Enter Roll No.: "))
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                city = input("Enter city: ")

                add_student(students, rollno, fname, lname, city)
                print("\nRecord successfully added\n")
            except (ValueError, Exception) as err:
                print(err)
        elif choice == "2":
            try:
                rollno = int(input("Enter Roll No.: "))
                show_student(students, rollno)
            except (ValueError, Exception) as err:
                print(err)
        elif choice == "3":
            try:
                rollno = int(input("Enter Roll No.: "))
                field_to_update = input("What field you want to update? (Valid choices: fname, lname, city): ")
                new_value = input("Enter new value for field '{}': ".format(field_to_update))
                update_student(students, rollno, field_to_update, new_value)
                print("\nRecord successfully updated\n")
            except (ValueError, Exception) as err:
                print(err)
        elif choice == "4":
            try:
                rollno = int(input("Enter Roll No.: "))
                delete_student(students, rollno)
                print("\nRecord successfully deleted\n")
            except (ValueError, Exception) as err:
                print(err)
        elif choice == "5":
            show_all_students(students)
        elif choice == "6":
            break
        else:
            print("\nWrong choice :(\n")


main()
