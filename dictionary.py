'''
thisdict= {
    "brand": "ford",
    "model":"Mustang",
    "year": 1984
}
x= thisdict["model"]
print(x)
#Both the above statement make a dictionary having 3 key-value pairs.
print(D['rollno'])
D['age']=28
'''
'''
# Define the student information
students = [
    {"roll_number": 101, "name": "Alice", "contact_number": "1234567890"},
    {"roll_number": 102, "name": "Bob", "contact_number": "9876543210"},
    {"roll_number": 103, "name": "Charlie", "contact_number": "5678901234"}
]

# Function to display student information
def display_students(student_list):
    for student in student_list:
        print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Contact Number: {student['contact_number']}")

# Display the student information
display_students(students)

'''

# Define the student information using a dictionary
students = {
    101: {"name": "Alice", "contact_number": "1234567890"},
    102: {"name": "Bob", "contact_number": "9876543210"},
    103: {"name": "Charlie", "contact_number": "5678901234"}
}

# Function to display student information
def display_students(student_dict):
    for roll_number, details in student_dict.items():
        print(f"Roll Number: {roll_number}, Name: {details['name']}, Contact Number: {details['contact_number']}")

# Function to add a new student
def add_student(roll_number, name, contact_number):
    students[roll_number] = {"name": name, "contact_number": contact_number}

# Function to update a student's details
def update_student(roll_number, name=None, contact_number=None):
    if roll_number in students:
        if name:
            students[roll_number]["name"] = name
        if contact_number:
            students[roll_number]["contact_number"] = contact_number

# Function to delete a student
def delete_student(roll_number):
    if roll_number in students:
        del students[roll_number]

# Adding a new student
add_student(104, "Daisy", "1122334455")
# Updating a student's details
update_student(101, contact_number="1111222233")
# Deleting a student
delete_student(103)

# Display the updated student information
display_students(students)
