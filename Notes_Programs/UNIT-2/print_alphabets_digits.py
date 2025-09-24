# Print alphabets and digits both comma-separated and space-separated with headings

# --- Uppercase Alphabets ---
print("Uppercase Alphabets:")
upper_comma = ""
upper_space = ""
for i in range(65, 91):  # ASCII A-Z
    upper_comma += chr(i)
    upper_space += chr(i) + " "
    if i != 90:
        upper_comma += ","
print("Comma-separated:", upper_comma)
print("Space-separated:", upper_space.strip())  # remove trailing space

# --- Lowercase Alphabets ---
print("\nLowercase Alphabets:")
lower_comma = ""
lower_space = ""
for i in range(97, 123):  # ASCII a-z
    lower_comma += chr(i)
    lower_space += chr(i) + " "
    if i != 122:
        lower_comma += ","
print("Comma-separated:", lower_comma)
print("Space-separated:", lower_space.strip())

# --- Digits ---
print("\nDigits:")
digits_comma = ""
digits_space = ""
for i in range(0, 10):
    digits_comma += str(i)
    digits_space += str(i) + " "
    if i != 9:
        digits_comma += ","
print("Comma-separated:", digits_comma)
print("Space-separated:", digits_space.strip())
