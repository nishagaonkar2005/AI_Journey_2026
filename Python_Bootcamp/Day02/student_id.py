first_name = "nisha"
middle_name = "dinesh"
last_name = "gaonkar"
usn = "2GP23CS062"
college_name = "govt engineering college majali, karwar"
address = "ashram road kajubag, karwar"
ph_no = "6360522939"

full_name = (first_name + " " + middle_name + " " + last_name).title()

print("===========================================")
print("STUDENT ID")
print("===========================================")


print("Name = ",full_name)
print("USN = ",usn)
print("College name = ", college_name.title())
print("Address= ", address.title())
print("Phone no = ", ph_no)

print(len(full_name))
print(full_name.strip())
print(full_name.find("h"))
print(first_name.replace("nisha", "Nishu"))
print(full_name[0:4])
print(full_name[:-4])
print(college_name[5])
print(full_name[-1:])
print(f"Name : {full_name}")
print(college_name[:-23])