import random

# Step 1: Create a list of 20 random numbers between 10 and 100
random_numbers = []
for i in range(20):
    num = random.randint(10, 100)
    random_numbers.append(num)

print("Original list:", random_numbers)

# Step 2: Filter out numbers strictly between 20 and 50
filtered_numbers = []
for num in random_numbers:
    if num <= 20 or num >= 50:
        filtered_numbers.append(num)

print("Filtered list (excluding 20 < num < 50):", filtered_numbers)



import random

# Step 1: Create a list of 20 random numbers between 10 and 100
random_numbers = [random.randint(10, 100) for _ in range(20)]
print("Original list:", random_numbers)

# Step 2: Filter out numbers strictly between 20 and 50
filtered_numbers = [num for num in random_numbers if num <= 20 or num >= 50]
print("Filtered list (excluding 20 < num < 50):", filtered_numbers)