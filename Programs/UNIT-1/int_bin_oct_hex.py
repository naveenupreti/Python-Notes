# Program: Conversion table of numbers into Binary, Octal, and Hexadecimal

# Take range input from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("\nNumber Conversion Table")
print("-" * 55)
print(f"{'Decimal':<10}{'Binary':<15}{'Octal':<15}{'Hexadecimal':<15}")
print("-" * 55)

# Loop through the range
for num in range(start, end + 1):
    binary = bin(num)[2:]       # remove '0b' prefix
    octal = oct(num)[2:]        # remove '0o' prefix
    hexa = hex(num)[2:].upper() # remove '0x' prefix, uppercase
    print(f"{num:<10}{binary:<15}{octal:<15}{hexa:<15}")

# Program: Conversion table of numbers into Binary, Octal, and Hexadecimal
# Compatible with Python 3.4

# Take range input from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("\nNumber Conversion Table")
print("-" * 55)
print("{:<10}{:<15}{:<15}{:<15}".format("Decimal", "Binary", "Octal", "Hexadecimal"))
print("-" * 55)

# Loop through the range
for num in range(start, end + 1):
    binary = bin(num)[2:]       # remove '0b' prefix
    octal = oct(num)[2:]        # remove '0o' prefix
    hexa = hex(num)[2:].upper() # remove '0x' prefix, uppercase
    
    print("{:<10}{:<15}{:<15}{:<15}".format(num, binary, octal, hexa))
