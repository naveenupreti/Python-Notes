'''
create two versions of a Strong Random Password Generator that always includes:

✅ at least 1 uppercase letter

✅ at least 1 lowercase letter

✅ at least 1 digit

✅ at least 1 special symbol

Version 1 – Without List Comprehension (simple)
Version 2 – With List Comprehension (compact)

'''
#Version 1 – Without List Comprehension
'''
Picks one character each from uppercase, lowercase, digits, and symbols to guarantee diversity.
Then fills the rest randomly.
Finally shuffles to randomize order, so the first 4 aren’t predictable.
Sample Output:
Enter password length (min 4): 10
Generated Strong Password: 7h@Akq!8Z2
'''
import random
import string

# Step 1: Define character groups
upper = string.ascii_uppercase       # 'A'–'Z'
lower = string.ascii_lowercase       # 'a'–'z'
digits = string.digits               # '0'–'9'
symbols = string.punctuation         # Special characters

# Step 2: Combine all character groups
all_chars = upper + lower + digits + symbols

# Step 3: Take password length from user
length = int(input("Enter password length (min 4): "))

# Step 4: Ensure minimum one from each category
password = random.choice(upper)
password += random.choice(lower)
password += random.choice(digits)
password += random.choice(symbols)

# Step 5: Fill remaining characters randomly
for i in range(length - 4):
    password += random.choice(all_chars)

# Step 6: Shuffle to mix character positions
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

# Step 7: Display result
print("Generated Strong Password:", password)


#Version 2 – With List Comprehension
import random
import string

# Define character sets
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation
all_chars = upper + lower + digits + symbols

length = int(input("Enter password length (min 4): "))

# Ensure one character from each set
password_chars = [
    random.choice(upper),
    random.choice(lower),
    random.choice(digits),
    random.choice(symbols)
]

# Add remaining characters using list comprehension
password_chars += [random.choice(all_chars) for _ in range(length - 4)]

# Shuffle and join
random.shuffle(password_chars)
password = ''.join(password_chars)

print("Generated Strong Password:", password)

