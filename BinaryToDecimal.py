# Input binary number as string
binary = input("Enter a binary number: ")

decimal = 0
position = 0

# Loop through binary digits from right to left
for digit in reversed(binary):
    decimal += int(digit) * (2 ** position)
    position += 1

print("Decimal value:", decimal)
