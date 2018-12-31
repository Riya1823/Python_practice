import sys


VALID_FIELDS = ("rollno", "fname", "lname", "city")


class StudentDataError(Exception):
    pass


class StudentNotFound(Exception):
    pass


class StudentInvalidField(Exception):
    pass


def _dict_to_line(data):
    return ",".join([data["rollno"], data["fname"], data["lname"], data["city"] + "\n"])


def _line_to_dict(csv_line):
    """Convert comma separated values into a dictionary

    Create a dictionary representing student data by using (pre-defined)fields
    and taking values from 'csv_line'

    Parameters:
        csv_line: A string of comma separated values

    Returns:
        A dictionary of pre-defined keys and values from 'csv_line'

    Raises:
        StudentDataError if there is a mismatch between no. of pre-defined keys
        and the no. of values in 'csv_line'
    """
    # remove leading/trailing newlines
    csv_line = csv_line.strip()
    values = csv_line.split(",")

    if len(values) != len(VALID_FIELDS):
        raise StudentDataError("ERROR: data in line '{}' is corrupt or not in correct format".format(csv_line))

    data = dict(zip(VALID_FIELDS, values))
    return data


def _find_student_data(file_path, rollno):
    with open(file_path) as file:
        for line in file:
            data = _line_to_dict(line)
            if data["rollno"] == rollno:
                return data


def _print_data(data):
    print("\n")
    print("ROLL NO.   : {}".format(data["rollno"]))
    print("FIRST NAME : {}".format(data["fname"]))
    print("LAST NAME  : {}".format(data["lname"]))
    print("CITY       : {}".format(data["city"]))


def usage():
    msg = """
    USAGE:
    {} <operation> [args for the operation]
    
    OPERATION   ARGS
    add         <rollno> <first name> <last name> <city>
    show        <rollno>
    showall
    update      <rollno> <"field1=new_val1"> <"field2=new_val2"> ...
    delete      <rollno>
    """.format(sys.argv[0])
    print(msg)


def add_student(file_path, values):
    data = {}
    for i, field in enumerate(VALID_FIELDS):
        data[field] = values[i]

    with open(file_path, "a") as file:
        line = _dict_to_line(data)
        file.write(line)


def show_student(file_path, rollno):
    data = _find_student_data(file_path, rollno)
    if data is None:
        raise StudentNotFound("ERROR: data for rollno '{}' not found".format(rollno))    
    _print_data(data)


def delete_student(file_path, rollno):
    found = False
    lines = []
    with open(file_path, "r+") as file:
        for line in file:
            # skip line for target rollno
            data = _line_to_dict(line)
            if data["rollno"] == rollno:
                found = True
                continue
            lines.append(line)

        if not found:
            raise StudentNotFound("ERROR: data for rollno '{}' not found".format(rollno))    
        # reset file pointer and delete all data in file
        file.seek(0)
        file.truncate(0)

        # write data line back to file
        for line in lines:
            file.write(line)


def show_all_students(file_path):
    with open(file_path) as file:
        for line in file:
            data = _line_to_dict(line)
            _print_data(data)


def update_student(file_path, rollno, field, value):
    if field not in VALID_FIELDS:
        raise StudentInvalidField("field '{}' not valid for student".format(field))

    found = False
    lines = []
    with open(file_path, "r+") as file:
        for line in file:
            # update line for target rollno
            data = _line_to_dict(line)
            if data["rollno"] == rollno:
                found = True
                data[field] = value
                line = _dict_to_line(data)
            lines.append(line)

        if not found:
            raise StudentNotFound("ERROR: data for rollno '{}' not found".format(rollno))    
        # reset file pointer and delete all data in file
        file.seek(0)
        file.truncate(0)

        # write data line back to file
        for line in lines:
            file.write(line)


def main():
    file_path = "students.csv"
    args = sys.argv
    if len(args) < 2:
        usage()
        sys.exit(1)

    operation = args[1]
    try:
        if operation == "add":
            if len(args) < 6:
                raise SystemExit("ERROR: all arguments for 'add' not provided")

            add_student(file_path, args[2:6])
        elif operation == "show":
            if len(args) < 3:
                raise SystemExit("ERROR: rollno not provided")

            rollno = args[2]
            show_student(file_path, rollno)
        elif operation == "showall":
            show_all_students(file_path)
        elif operation == "update":
            if len(args) < 5:
                raise SystemExit("ERROR: all arguments for 'update' not provided")
            rollno, field, value = args[2:5]
            update_student(file_path, rollno, field, value)
        elif operation == "delete":
            if len(args) < 3:
                raise SystemExit("ERROR: rollno not provided")

            rollno = args[2]
            delete_student(file_path, rollno)
        else:
            print("ERROR: Unknow operation!")
    except (IOError, StudentNotFound, StudentDataError, StudentInvalidField) as err:
        print(err)


if __name__ == "__main__":
    main()
