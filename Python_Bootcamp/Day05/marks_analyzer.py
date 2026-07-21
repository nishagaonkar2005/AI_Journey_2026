marks1 = int(input("Enter marks for 1st language:"))
marks2 = int(input("Enter marks for 2nd language:"))
marks3 = int(input("Enter marks for 3rd language:"))
marks4 = int(input("Enter marks for maths:"))
marks5 = int(input("Enter marks for science:"))
marks6 = int(input("Enter marks for social studies:"))

total = marks1 + marks2 + marks3 + marks4 + marks5 + marks6
average = total / 6
percentage = total / 600 * 100

marks = [marks1, marks2, marks3, marks4, marks5, marks6]

for mark in marks:
    print(mark)

print(f"1st language :{marks1}")
print(f"2nd language :{marks2}")
print(f"3rd language :{marks3}")
print(f"Maths :{marks4}")
print(f"Science :{marks5}")
print(f"Social studies :{marks6}")
print(f"Total :{total}")
print(f"Average :{average}")
print(f"Percentage :{percentage:.2f}%")

print(f"Heighest marks :{max(marks)}")
print(f"Lowest marks :{min(marks)}")
print(f"No of subject's :{len(marks)}")


#list.append()- adds elements in list
#list.insert()- inserts elements in order based on index numbers
#list.remove()- deletes the element
#list.po()- removes/deletes last element