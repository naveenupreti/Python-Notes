"""
Demonstration that strings in Python are immutable.
"""

def main() -> None:
    # Original string
    my_string = "Hello"
    print("Original string:", my_string)

    try:
        # Attempt to change the first character
        my_string[0] = "h"
    except TypeError as error:
        print("Error occurred:", error)

    # Correct way to modify a string: create a new string
    new_string = "h" + my_string[1:]
    print("Modified string by creating new string:", new_string)


if __name__ == "__main__":
    main()
