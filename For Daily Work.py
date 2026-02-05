
class University:

    def __init__(self, name, total_students):
        self.name = name
        self.total_students = total_students

    # Inner class
    class Department:
        def __init__(self, university, department_name):
            self.university = university
            self.department_name = department_name

        def display_info(self):
            print("University Name:", self.university.name)
            print("Total Students:", self.university.total_students)
            print("Department Name:", self.department_name)


# Creating object of outer class
uni = University("Kabul University", 12000)

# Creating object of inner class
dept = University.Department(uni, "Computer Science")

# Calling method
dept.display_info()
