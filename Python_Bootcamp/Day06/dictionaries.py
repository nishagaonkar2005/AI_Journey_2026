student = {
    "name" : "Nisha D G",
    "usn" : "2GP23CS062",
    "semester" : 7,
    "branch" : "Computer Science Engineering",
    "college" : "Government Engineering College Majali, Karwar",
    "age" : 21
}

print(f"Name :",student["name"])
print(f"USN :",student["usn"])
print(f"Semester :",student["semester"])
print(f"Branch :",student["branch"])
print(f"College :",student["college"])
print(f"Age :",student["age"])

student["phone_no"] =6360522939    #adding the elements/altering the elements
print(f"Phone no :",student["phone_no"])

#shows the difference befor and after deleting the 'age'
print("Before deleting the age")
print(student)

del student["age"]               #deleting the element

print("\nAfter deleting the age")
print(student)