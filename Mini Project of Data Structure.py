
# Mini Projects for Data Structure 
students = { 
    "Alice": [85, 90, 78], 
    "Bob": [70, 68, 72], 
} 
 
def add_student(name): 
    if name not in students: 
        students[name] = [] 
    else: 
        print(f"{name} already exists.") 
 
def add_grade(name, grade): 
    if name in students: 
        students[name].append(grade) 
    else: 
        print(f"Student {name} not found.") 
 
def average_grade(name): 
    grades = students.get(name) 
    if grades: 
        return sum(grades) / len(grades) 
    return None 
 
def passed(name): 
    avg = average_grade(name) 
    return avg is not None and avg >= 60 
 
# Adding a new student and grades 
add_student("Charlie") 
add_grade("Charlie", 95) 
add_grade("Charlie", 20) 
 
# Print report 
for student in students: 
    avg = average_grade(student) 
    status = "Passed" if passed(student) else "Failed" 
    print(f"{student}: Avg Grade = {avg:.2f}, Status = {status}") 