class Student:
    def __init__(self, name, age, grade):
        self.name = name  # Store the student's name
        self.age = age    # Store the student's age
        self.grade = grade  # Store the student's grade

    def display_info(self):
        # Display the student's information
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentDatabase:
    def __init__(self):
        self.students = []  # Initialize a list to hold student objects

    def add_student(self, name, age, grade):
        # Check if we already have 5 students
        if len(self.students) < 5:
            new_student = Student(name, age, grade)  # Create a new Student object
            self.students.append(new_student)  # Add it to the list
        else:
            print("Database is full! Cannot add more students.")

    def display_students(self):
        # Display all students in the database
        if not self.students:
            print("No students to display.")
            return
        
        for index, student in enumerate(self.students, start=1):
            print(f"Student {index}: {student.display_info()}")


# Example Usage
database = StudentDatabase()

# Adding students
database.add_student("Bankim", 20, "A")
database.add_student("Sneha", 22, "B")
database.add_student("rohan", 21, "C")
database.add_student("rohit", 23, "B")
database.add_student("om", 19, "A")

# Trying to add a sixth student
database.add_student("Frank", 24, "C")  # This should give an error message

# Displaying students
database.display_students()
