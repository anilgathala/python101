### Take an integer as an input and print its square
# Reading an integer
a = int(input("Enter integer to square: "))
print("square: ", a * a)

### Take two integers as input (one by one) and print their sum and product in separate lines
# Reading an integer
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
print("    sum: ", x + y)
print("product: ", x * y)

### Take four integers as input (all provided in one line and separated by space) and print their average.
# Reading an integer
values = input("Enter four integers, separated by space in the same line: ").split()
p = int(values[0])
q = int(values[1])
r = int(values[2])
s = int(values[3])
avg = float(p + q + r + s) / 4.0
print("   Avg: ", avg)

