'''
create two versions of a Strong Random Password Generator that always includes:

✅ at least 1 uppercase letter

✅ at least 1 lowercase letter

✅ at least 1 digit

✅ at least 1 special symbol

Version 1 – Without List Comprehension (simple)
Version 2 – With List Comprehension (compact)

Logic:
Picks one character each from uppercase, lowercase, digits, and symbols to guarantee diversity.
Then fills the rest randomly.
Finally shuffles to randomize order, so the first 4 aren’t predictable.

'''
#Random Password Generator that Stops When User Wants
import random
import string

# Define character sets
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation
all_chars = upper + lower + digits + symbols

print("=== STRONG PASSWORD GENERATOR ===")

while True:
    print("\nChoose Password Generator Type:")
    print("1. Simple Method (without list comprehension)")
    print("2. Compact Method (with list comprehension)")

    # ✅ Safely get user choice
    choice_input = input("Enter your choice (1 or 2): ").strip()
    if not choice_input.isdigit():
        print("❌ Invalid input! Please enter a number (1 or 2).")
        again = input("\nDo you want to try again? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("\nThank you for using the Password Generator. Goodbye!")
            break
        else:
            continue

    choice = int(choice_input)

    # ✅ Validate choice number
    if choice not in (1, 2):
        print("❌ Invalid choice! Please enter 1 or 2.")
        again = input("\nDo you want to try again? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("\nThank you for using the Password Generator. Goodbye!")
            break
        else:
            continue

    # ✅ Get password length (only if choice is valid)
    while True:
        length_input = input("Enter password length (min 4): ").strip()
        if not length_input.isdigit():
            print("❌ Please enter a valid number.")
            continue
        length = int(length_input)
        if length < 4:
            print("❌ Password length must be at least 4.")
        else:
            break

    # --- Version 1: Without list comprehension ---
    if choice == 1:
        password = random.choice(upper)
        password += random.choice(lower)
        password += random.choice(digits)
        password += random.choice(symbols)

        for i in range(length - 4):
            password += random.choice(all_chars)

        # Shuffle to mix characters
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        print("\nGenerated Strong Password (Simple):", password)

    # --- Version 2: With list comprehension ---
    elif choice == 2:
        password_chars = [
            random.choice(upper),
            random.choice(lower),
            random.choice(digits),
            random.choice(symbols)
        ]
        password_chars += [random.choice(all_chars) for _ in range(length - 4)]
        random.shuffle(password_chars)
        password = ''.join(password_chars)

        print("\nGenerated Strong Password (Compact):", password)

    # ✅ Ask user if they want to continue
    again = input("\nDo you want to generate another password? (y/n): ").strip().lower()
    if again not in ('y', 'yes'):
        print("\nThank you for using the Password Generator. Goodbye!")
        break


