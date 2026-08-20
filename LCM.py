# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Step 1: Find GCD using Euclidean algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

# Step 2: Compute LCM
lcm = (a * b) // gcd

# Output result
print("LCM of", a, "and", b, "is:", lcm)
