secret_number = 7
guess = int(input("Enter a number:"))
while guess != secret_number:
    print("wrong!!")
    guess = int(input("Try again:"))
    print("Correct!!")
