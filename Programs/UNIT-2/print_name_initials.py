# Program: Convert "First Middle LastName" into initials format
# Rule: All words except the last become initials, last word in full with proper capitalization

# Take input from user
name = input("Enter your full name: ")

# Step 1: Remove extra spaces (both ends + in between)
#  - strip() removes spaces from start and end
#  - split() breaks into words, ignoring multiple spaces
#  - join() rebuilds with single spaces
name = " ".join(name.strip().split())

# Step 2: Split into words
parts = name.split(" ")

# Step 3: Process initials + last name
if len(parts) == 1:
    # If only one word, just capitalize it
    result = parts[0].capitalize()
else:
    # Create initials for all words except last
    initials = ""
    for word in parts[:-1]:   # everything except the last word
        initials += word[0].upper() + ". "  # take first letter as uppercase + ". "
    
    # Format last name with first letter uppercase, rest lowercase
    last_name = parts[-1].capitalize()

    # Combine initials with last name
    result = initials + last_name

# Step 4: Print the result
print(result)
