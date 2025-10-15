'''
Convert the String "International" into a tuple and then add ! at the end.
Now print the frequency and positions of the duplicate letters in that.
'''
# Step 1: Convert string to tuple and add '!'
s = "International"
t = tuple(s) + ('!',)
print("Tuple:", t)

# Step 2: Find duplicates and their positions
checked = []  # To keep track of letters we've already processed

for i in range(len(t)):
    char = t[i]
    if char in checked:
        continue  # Skip letters we've already processed
    
    # Find all positions of this character
    positions = []
    for j in range(len(t)):
        if t[j] == char:
            positions.append(j)
    
    # If more than 1 occurrence, print
    if len(positions) > 1:
        print(f"Letter '{char}' appears {len(positions)} times at positions {positions}")
    
    checked.append(char)  # Mark this character as processed
'''
Output:
Tuple: ('I', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'a', 'l', '!')
Letter 'n' appears 3 times at positions [1, 5, 10]
Letter 't' appears 2 times at positions [2, 7]
Letter 'a' appears 2 times at positions [6, 11]
'''