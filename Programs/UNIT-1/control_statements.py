'''
                                    Control Structures in Python
                                    
Control structures in programming determine the flow of execution of the code.
They allow a program to make decisions, repeat tasks, or skip certain parts.

In Python, the main types of control structures are:

Decision-making statements: if, if-else, elif, nested if

Looping statements (Iteration): for, while

Loop control statements: break, continue, pass


if-else Statement

The if-else statement is used to execute a block of code if a condition is True, and another block if the condition is False.

Syntax:

if condition:
    # code if condition is True
else:
    # code if condition is False


Example:
'''
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

'''
Output:

You are eligible to vote.

elif Statement

elif (else if) allows checking multiple conditions. Python executes the block of the first true condition.

Syntax:

if condition1:
    # code
elif condition2:
    # code
else:
    # code


Example:
'''
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

'''
Output:

Grade B

Nested if

A nested if is an if statement inside another if statement. It allows more detailed checking.

Example:
'''
num = 10
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")

'''
Output:

Positive number
Even number

Iteration Control Structures (Loops)

Python has for and while loops to repeat code multiple times.

For loop example:
'''
for i in range(3):
    print("Hello", i)

'''
Output:

Hello 0
Hello 1
Hello 2


While loop example:
'''
count = 0
while count < 3:
    print("Count:", count)
    count += 1

'''
Output:

Count: 0
Count: 1
Count: 2

break Statement

break stops the loop immediately, even if the loop condition is still True.

Example:
'''
for i in range(5):
    if i == 3:
        break
    print(i)

'''
Output:

0
1
2

continue Statement

continue skips the current iteration and moves to the next iteration of the loop.

Example:
'''
for i in range(5):
    if i == 2:
        continue
    print(i)

'''
Output:

0
1
3
4

pass Statement
pass does nothing. It's used as a placeholder when a statement is required syntactically but you don’t want any code to execute.

Example:
'''
num = 10
if num > 0:
    pass  # Will do nothing
else:
    print("Negative")

'''
Output:

# Nothing is printed
'''
#Example Mixing All Control Structures
students = [
    {"name": "Alice", "marks": 95},
    {"name": "Bob", "marks": 67},
    {"name": "Charlie", "marks": 82},
    {"name": "David", "marks": 45},
    {"name": "Eve", "marks": 75}
]

for student in students:
    name = student["name"]
    marks = student["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    # Nested if to check for distinction
    if grade in ["A", "B"]:
        if marks >= 90:
            print(f"{name} scored {marks} - Excellent! Grade: {grade}")
        else:
            print(f"{name} scored {marks} - Good job! Grade: {grade}")
    else:
        # Use pass as a placeholder for future logic
        pass

    # Skip students who failed
    if grade == "F":
        continue

    # Stop processing if a student has perfect marks
    if marks == 100:
        print("Found a student with perfect score! Ending loop.")
        break

'''
Output:

Alice scored 95 - Excellent! Grade: A
Charlie scored 82 - Good job! Grade: B
Eve scored 75 - Good job! Grade: B


Explanation:

if-elif-else determines the grade.

Nested if prints different messages based on marks.

pass is used for students who don’t need extra processing.

continue skips failed students.

break stops the loop if someone has perfect marks.
'''