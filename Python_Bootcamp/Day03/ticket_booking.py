age = int(input("Enter the valid age:"))
tickets = int(input("Enter the no of tickets:"))

if age < 5:
    amount = 0
elif 5 <= age <= 17:
    amount = 170
elif 18 <= age <= 59:
    amount = 200
elif age >= 60:
    amount = 150
else:
    amount = 150

total_amount =  amount * tickets

print("======================================")
print("Movie Ticket")
print("======================================")

print(f"Age :{age}")
print(f"Tickets :{tickets}")
print(f"Price per ticket :₹{amount}")
print(f"Total_amount :₹{total_amount}")