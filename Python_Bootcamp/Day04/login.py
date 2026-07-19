User_name = "nishu"
Password = "nish123"

username = input("Enter username:")
password = input("Enter password:")

while username != User_name or password != Password:
    if username != User_name or password != Password:
        print("Invalid username or password ❌")

    username = input("Enter username again:")
    password = input("Enter password again:")

print("Login successful ✅")

