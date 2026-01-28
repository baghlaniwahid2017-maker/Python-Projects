
#Dictionary worked and practiced.
#student = {
#   "Name": "Wahid",
#    "Age": 32,
#    "dob": "1993/03/10",
#    "Email": "Baghlaniwahid2017@gmail.com"
#}
#print(student)
#print(student.get("Age"))
#print(student.values())
#print(student.keys())
#print(student.items())
#student.update({"Gender": ""})
#student.pop("Age")
#print(student)

student = {
    "Name": "Wahid",
    "Age": 32,
    "dob": "1993/03/10",
    "Email": "Baghlaniwahid2017@gmail.com"
}
#print(student)
#print(student.get("dob"))
#print(student.values())
#print(student.keys())
#student.update({"sex":"Male"})
#print(student)
#student.pop("Email")
#print(student)

# Nested Dictionary ( is used for complex data)

#students = {
#    "Ahmad": {"Age": 30, "Grade":95},
#    "Wahid": {"Age": 32, "Grade":99},
#    "Ali": {"Age": 44, "Grade": 88}
#}

#print(students["Ahmad"]["Age"])
#print(students["Wahid"]["Grade"])
#print(students["Ali"]["Age"])


# Sets

fruits = {"Apple", " Orange", " Banana", "lemon"}
#fruits.add("Cheery") ( add new set or item)
#fruits.remove("Apple") ( remove specific set or item)
#fruits.discard("Apple") ( remove specific ser or item with no error to show)
fruits2 = {"lemon", " Avocado", "Apple"}
#print(fruits.union(fruits2)) ( it combine both sets)
#print(fruits.difference(fruits2)) ( is show the defirences of set one which fruits from set two which is fruits2, it mean those who are in set a and set b, the remaing of a is shown)
#print(fruits.intersection(fruits2)) ( is show the items which are in both sets)
print(fruits.symmetric_difference(fruits2))