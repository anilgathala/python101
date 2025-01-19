# Reading a string
name = input("Enter your name: ")

# Reading an integer
age = int(input("Enter your age: "))

# Reading a float
height = float(input("Enter your height in meters: "))

# Reading multiple values (separated by spaces)
values = input("Enter three numbers separated by spaces: ").split()
num1 = int(values[0])
num2 = int(values[1])
num3 = int(values[2])

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Numbers:", num1, num2, num3)
