# -------------------------------------------------------------
# Program: Important string module functions + OUTPUT
# -------------------------------------------------------------
import string

# ascii letters
print("ASCII letters:", string.ascii_letters)

# lowercase and uppercase
print("\nLowercase:", string.ascii_lowercase)
print("Uppercase:", string.ascii_uppercase)

# digits
print("\nDigits:", string.digits)

# punctuation
print("\nPunctuation characters:", string.punctuation)

# whitespace characters
print("\nWhitespace chars:", repr(string.whitespace))

# capwords() – capitalizes each word
text = "welcome to python programming"
print("\nCapwords:", string.capwords(text))

# Template class – string formatting
from string import Template

t = Template("Hello $name, your score is $score")
msg = t.substitute(name="Naveen", score=95)
print("\nTemplate output:", msg)


# -------------------------------------------------------------
# SAMPLE OUTPUT
# -------------------------------------------------------------
"""
ASCII letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Lowercase: abcdefghijklmnopqrstuvwxyz
Uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Digits: 0123456789

Punctuation characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

Whitespace chars: '\t\n\x0b\x0c\r '

Capwords: Welcome To Python Programming

Template output: Hello Naveen, your score is 95
"""
