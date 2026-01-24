# get method challenge
# Challenge: Safely look up student info using get()

# step 1: Dictionary of students
students={
    "s001":{"name":"Asha","age":20,"grade":"A"},
    "s002":{"name":"Berlin","age":25,"grade":"B"},
    "s003":{"name":"Tania","age":18,"grade":"F"}
}

# Step 2: Ask user for student ID
student_id=input("Enter student ID (e.g.,s001):")

# step 3: safely get student info
student_info=students.get(student_id)

if student_info:
    # print all info using get() safely

    name=student_info.get("name","Name not available")
    age=student_info.get("age","Age not available")
    grade=student_info.get("grade","Grade not available")

    print(f"Name: {name}\nAge: {age}\nGrade: {grade}")
else:
    print("Student ID not found. Try again!")


# sample output:

# Enter student ID (e.g.,s001):s002
# Name: Berlin
# Age: 25
# Grade: B
#---------------------------------
# Enter student ID (e.g.,s001):s004
# Student ID not found. Try again!