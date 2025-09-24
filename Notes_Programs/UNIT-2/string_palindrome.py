"""
Program to check whether a given string is a palindrome.
Follows PEP 8 style guidelines.
Examples of Palindrome strings:

madam
level
rotator
racecar
malayalam
nitin
Was it a car or a cat I saw

"""


def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome.

    Args:
        text (str): Input string to check.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()

    # Reverse the string
    reversed_text = cleaned_text[::-1]

    # Compare original and reversed strings
    if cleaned_text == reversed_text:
        return True
    else:
        return False


def main() -> None:
    """Main function to take user input and display result."""
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()
