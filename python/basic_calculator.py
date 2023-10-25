# Define the functions for each operation
def add(x, y):
return x + y

def subtract(x, y):
return x - y

def multiply(x, y):
return x * y

def divide(x, y):
return x / y

# Ask the user to choose an operation
print("Please choose an operation:")
print("1. Add")
print("2. Subtract")
print(" . Multiply")
print("4. Divide")

# Get the user's choice and validate it
choice = input("Enter your choice (1/2/ /4): ")
if choice not in ("1", "2", " ", "4"):
print("Invalid input")
else:
# Get the user's numbers and validate them
try:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
except ValueError:
print("Invalid input. Please enter a number.")
else:
# Perform the calculation and display the result
if choice == "1":
result = add(num1, num2)
print(f"{num1} + {num2} = {result}")
elif choice == "2":
result = subtract(num1, num2)
print(f"{num1} - {num2} = {result}")
elif choice == " ":
result = multiply(num1, num2)
print(f"{num1} * {num2} = {result}")
elif choice == "4":
result = divide(num1, num2)
print(f"{num1} / {num2} = {result}")
