'''
1 __name__

__name__ is a special built-in variable in Python.

It tells Python how a script is being executed.

There are two main cases:

How the script runs	Value of __name__
Running the script directly	"__main__"
Importing the script as a module	The module’s filename (without .py)

2️== "__main__"

This checks if the script is being run directly.

If __name__ == "__main__" is True, it means you are running this file, not importing it somewhere else.

If the file is imported in another script, this condition is False, so the code inside this block won’t run automatically.

3️main()

main() is just a function we defined to hold the main logic of the program.

Writing the main logic in a function (instead of directly at the top level) is a good practice because:

Keeps code organized.

Makes it reusable.

Helps avoid accidental execution if the file is imported elsewhere.

4️ Why this is useful

Without this guard:

# If we just wrote
main()


The program would always run even if someone imported your script as a module in another program.

Using if __name__ == "__main__": ensures your program runs only when intended.

Example

file1.py:

def main():
    print("Hello from file1")

print("This always runs")

if __name__ == "__main__":
    main()


Case 1 – Run directly:

python file1.py


Output:

This always runs
Hello from file1


Case 2 – Import in another file:

# file2.py
import file1


Output when running file2.py:

This always runs


Notice main() from file1 did not run because of the if __name__ == "__main__": guard.

✅ Summary

__name__ == "__main__" → “Am I running directly?”

main() → “Run the main function only if I’m running directly.”

Keeps your code modular, safe, and reusable.
'''