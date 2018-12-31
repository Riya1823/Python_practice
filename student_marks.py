marks = int(input("Enter Marks"))
while n<=100:
    if marks < 40:
        print("fail")
    elif marks < 50 or marks > 40:
        print("pass class")
    elif marks < 60 or marks > 50:
        print("second class")
    elif marks < 70 or marks > 60:
        print("first class")     
    elif marks > 70:
        print("Pass with Distion")
