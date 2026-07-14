name = input("Enter the student's name:").title()
roll_no = int(input("Enter roll_no:"))
std = input ("Enter the standard :")
div = input("Enter the division:").upper()

English = int(input("Enter mark's of English :"))
Kannada = int(input("Enter mark's of Kannada :"))
Hindi = int(input("Enter mark's of Hindi :"))
Mathematics= int(input("Enter mark's of Maths :"))
Science = int(input("Enter mark's of Science :"))
Social_Science = int(input("Enter mark's of Social :"))

total_marks = English + Kannada + Hindi + Mathematics + Science + Social_Science
average = total_marks / 6
percentage = (total_marks / 600) * 100

print("===================================================")
print("Student's Marks Card")
print("===================================================")

print(f" Name : {name}")
print(f" Roll_no : {roll_no}")
print(f" Std : {std}")
print(f" Div : {div}")

print(f"Total_marks : {total_marks}")
print(f"Average : {average:.2f}")
print(f"Percentage : {percentage:.2f}")

if average >= 90:
    print("Topper")
elif average >= 75:
    print("FCD")
elif average == 70:
    print("FC")
else:
    print("Fail")