'''
The random module in Python is used to generate random numbers
or make random selections — useful in games, simulations, testing, or sampling.

random() → always between 0 and 1

uniform(a, b) → float between a and b inclusive

randint(a, b) → integer between a and b inclusive

randrange(start, stop, step) → similar to range() but returns a random item
between start and stop exclusive. Both range() and randrange() always return an integer 

choice(seq) → picks one random element

shuffle(list) → rearranges items randomly (changes the original list)

sample(seq, n) → picks n unique items

seed(value) → same random result every time (useful in experiments or demos)

'''
'''
🎯 1. Import the random module
import random

🎲 2. Generate random numbers
a) Random float between 0 and 1
print(random.random())     # e.g. 0.7438

b) Random float in a given range
random.uniform(a, b) returns a random float number between a and b, inclusive of both ends.
That means:
    a<= N <=b   (a and b both inclusive)
print(random.uniform(10, 20))   # e.g. 14.68

c) Random integer in a range (inclusive)

random.randint(a, b) returns a random integer between a and b inclusive.
Both ends are included: you could get either a or b as the result.

print(random.randint(1, 6))     # simulates a dice roll (1–6)

d) Random integer in a range with step

random.randrange() returns a random integer from a given range, similar to Python’s built-in range() function.

The upper limit is exclusive, unlike randint().

🧩 Syntax
random.randrange(start, stop[, step])

Parameter			Meaning
start			Starting value of the range (inclusive)
stop			End of the range (exclusive)
step			Optional. Step size between values (default is 1)

print(random.randrange(0, 10, 2))   # picks from 0, 2, 4, 6, 8

🎴 3. Random choice from a sequence

random.choice() is used to pick one random element from a sequence (like a list, tuple, or string)
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))

🔀 4. Shuffle a list (in place)
random.shuffle() is used to rearrange the elements of a list randomly.

random.shuffle() shuffles a list in-place, meaning it changes the original list so that the order of elements becomes random.
It works only on mutable sequences (like lists), not tuples or strings.

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

🎯 5. Select multiple random items
random.sample() returns a list of unique random elements from a given sequence (like list, tuple, or string).

Syntax
random.sample(population, k)

Parameter			Meaning
population		The sequence (list, tuple, string, etc.) to pick from
k				Number of unique elements you want to pick

Returns a new list of length k
If k is larger than the size of the sequence → raises a ValueError

students = ["Amit", "Ravi", "Neha", "Kavya", "Tina"]
winners = random.sample(students, 2)   # pick 2 unique names
print(winners)

🎰 6. Set a seed (for reproducible results)

If you want the same “random” output each time:
seed(int) fixes the random generator’s starting point so you get the same random sequence every time you run the program
random.seed(10)
print(random.randint(1, 100))

random.seed(None) will produce a different number every time
print(random.randint(1, 100))
'''
#Example Program (All-in-One)

import random

# Random numbers
print("Random float:", random.random())
print("Random float rounded:", round(random.random(), 2))
print("Random float (10-20):", random.uniform(10, 20))
print("Random float (10-20) rounded:", round(random.uniform(10, 20), 3))
print("Random integer (1-6):", random.randint(1, 6))
print("Random even number (0-10):", random.randrange(0, 10, 2))
print("Random odd number (1-10):", random.randrange(1, 10, 2))
# Random choice
colors = ["red", "blue", "green", "yellow"]
print("Random color:", random.choice(colors))

# Shuffle
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# Sample
names = ["Amit", "Ravi", "Neha", "Kavya", "Tina"]
print("Random sample:", random.sample(names, 3)) # will return 3 random samples from the list

# Set seed for reproducibility
#random.seed(None)
random.seed(5)
print("Same random number each time:", random.randint(1, 100))


