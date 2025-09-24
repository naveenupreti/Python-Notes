#!/usr/bin/env python3
"""
Chapter 4 — Strings: Examples + Exercises (single script)

This single Python script collects the example programs from the
chapter on strings and solves the end-of-chapter exercises (A & B).
Every important statement is explained with an inline comment. The
comments follow PEP8 guidance for inline comments (separated from
code by two spaces and beginning with a #).

Note: This file is intended to be read and executed with Python 3.
"""

# A short helper to print section separators and titles for clarity.

def print_section(title: str) -> None:
    """Print a titled section separator for human-readable output.

    Args:
        title: The title of the section to display.
    """
    print('\n' + '=' * 70)  # visually separate sections when output grows
    print(title)  # show the section title so the output is self-describing
    print('-' * 70)  # underline the title for readability


# -----------------------------
# 1. Simple string creation
# -----------------------------

def example_simple_strings() -> None:
    """Demonstrate simple, raw and multiline string creation.

    Each line below contains an inline comment explaining what's
    happening so a reader can follow the idea without the chapter.
    """
    print_section('Example: simple and multiline strings')

    # Create a basic string using double quotes and assign to msg.
    msg = "Hoopla"  # a normal string literal assigned to variable `msg`
    print(msg)  # print the string value stored in `msg`

    # Create a string that contains embedded quotes by escaping them.
    msg2 = 'He said, "Let Us Python"'  # escape inner double quotes with backslash
    print(msg2)  # prints the string with quotes preserved

    # Create the same string using opposite outer quotes (no escaping needed).
    msg3 = "He said, 'Let Us Python'"  # using double quotes outside avoids escapes
    print(msg3)  # prints the same text but with single quotes inside

    # Raw string: backslashes are treated literally (useful for paths).
    raw_path = r"C:\temp\newfile"  # r-prefix prevents Python from treating \ as escape
    print(raw_path)  # prints the raw Windows-style path string

    # Triple quoted string (multiline literal) — newlines are preserved.
    poem = (
        """What is this life if full of care...\n"
        "We have no time to stand and stare"""
    )  # triple quotes define a multiline string literal
    print(poem)  # when printed it preserves the new line(s)

    # Adjacent string literals are concatenated at compile time.
    # This is a way to break long string literals across lines.
    long_piece = ("This is a long piece of text that "
                  "Python concatenates when literals are adjacent.")
    print(long_piece)  # prints the concatenation of the adjacent literals

    # Replication: multiply a string to print it repeatedly.
    rep = "Hoopla" * 3  # the string is repeated 3 times to produce a new string
    print(rep)  # prints 'HooplaHooplaHoopla'


# -----------------------------
# 2. Indexing and slicing
# -----------------------------

def example_indexing_slicing() -> None:
    """Show positive & negative indexing and different slicing forms."""
    print_section('Example: indexing and slicing')

    s = "Hello"  # store a 5-character string in `s`

    # Positive indexing starts from 0 — access the first and last char.
    first_char = s[0]  # first character 'H' is at index 0
    last_char = s[4]  # last character 'o' is at index 4 (0-based)
    print(first_char, last_char)  # prints 'H o'

    # Negative indices count from the right; -1 is last char.
    neg_first = s[-5]  # -5 indexes the leftmost char in this 5-char string
    neg_last = s[-1]  # -1 indexes the rightmost char
    print(neg_first, neg_last)  # prints 'H o'

    # Slicing: s[start:end] returns substring from start (incl.) to end (excl.).
    sub = s[1:4]  # characters at indices 1,2,3 -> 'ell'
    print(sub)  # prints 'ell'

    # Open-ended slices are allowed; omissions default to start or end.
    from_start = s[:2]  # from beginning up to index 2 (excl.) -> 'He'
    to_end = s[2:]  # from index 2 to end -> 'llo'
    full = s[:]  # complete copy of the string
    print(from_start, to_end, full)  # prints 'He llo Hello'

    # Large indices in plain indexing raise IndexError, but slicing tolerates
    try:
        _ = s[100]  # this will raise IndexError because index is too large
    except IndexError:
        print('IndexError: single-index access with an out-of-range index')

    # Slicing with out-of-range indices returns available portion without error.
    print(s[1:100])  # slice returns 'ello' rather than raising an error


# -----------------------------
# 3. Immutability, concatenation, membership
# -----------------------------

def example_immutability_concat_membership() -> None:
    """Demonstrate that strings are immutable and show concatenation.

    Also demonstrate membership test with `in` operator.
    """
    print_section('Example: immutability, concat & membership')

    s = "Hello"  # original string assigned to variable s

    # Strings do not support item assignment — attempting to mutate raises TypeError.
    try:
        s[0] = 'M'  # attempt to change the first character (not allowed)
    except TypeError:
        print('TypeError: strings are immutable; individual characters cannot be assigned')

    # Variables can be rebound to new string objects using concatenation.
    s = "Utopia"  # rebind the name s to a new string object 'Utopia'
    t = "Today!!!"  # another string
    s = s + t  # concatenation produces a brand-new string object assigned to s
    print(s)  # prints 'UtopiaToday!!!'

    # Membership test: check whether a substring exists in a string using `in`.
    print('e' in 'Hello')  # prints True because 'e' occurs in 'Hello'
    print('z' in 'Hello')  # prints False because 'z' is not in 'Hello'


# -----------------------------
# 4. Built-in functions and type information
# -----------------------------

def example_builtins_type_id() -> None:
    """Use len, min, max, type and id on strings to show properties."""
    print_section('Example: built-ins, type and id')

    msg = "Surreal"  # example string
    print('length:', len(msg))  # len() returns number of characters
    print('min char (by Unicode):', min(msg))  # smallest character by code point
    print('max char (by Unicode):', max(msg))  # largest character by code point

    # type() shows the object's type and id() shows its memory identity (address).
    print('type(msg):', type(msg))  # will print <class 'str'>
    print('id(msg):', id(msg))  # id is a numeric identifier for the object


# -----------------------------
# 5. Common string methods
# -----------------------------

def example_string_methods() -> None:
    """Show replace, join and several content-test methods with examples."""
    print_section('Example: string methods (replace, join, tests)')

    msg = 'Hello'  # example string for method demonstrations

    # replace(old, new) substitutes occurrences of old substring with new.
    print(msg.replace('l', 'L'))  # 'HeLLo' — replaces all 'l' with 'L'

    # join(iterable) joins each element of the iterable using the string as separator.
    joined = '|'.join('Hello')  # joins characters of 'Hello' with '|' between them
    print(joined)  # prints 'H|e|l|l|o'

    # Content-testing methods examples: isalpha, isdigit, isalnum, islower, isupper.
    a = 'NitiAayog'  # mixed-case alphabetic string
    b = '12345'  # numeric string
    c = 'ABC123'  # alphanumeric string
    print('isalpha:', a.isalpha(), b.isalpha())  # True for a, False for b
    print('isdigit:', b.isdigit(), c.isdigit())  # True for b, False for c
    print('isalnum:', a.isalnum(), b.isalnum(), c.isalnum())  # True for all that lack spaces
    print('islower/upper:', a.islower(), a.isupper())  # both False for mixed case


# -----------------------------
# 6. Case conversions and search/replace utilities
# -----------------------------

def example_conversions_search_trim_split() -> None:
    """Demonstrate case conversions, search/replace, trimming and splitting."""
    print_section('Example: conversions, find/replace, trim, split')

    s = 'Bring It On'  # sample phrase for multiple transformations

    # Case conversions
    print('upper():', s.upper())  # convert all characters to uppercase
    print('lower():', s.lower())  # convert all characters to lowercase
    print('capitalize():', s.capitalize())  # uppercase only the first character
    print('title():', s.title())  # uppercase first character of every word
    print('swapcase():', s.swapcase())  # swap case of each letter

    # find(sub) returns index of first occurrence or -1 if not found
    print('find "I" ->', s.find('I'))  # location of the first 'I' in the string
    print('find "On" ->', s.find('On'))  # location of substring 'On'

    # replace(old, new) produces a new string with replacements
    print('replace "It"->"Him":', s.replace('It', 'Him'))

    # trimming whitespace from left and right using lstrip, rstrip, strip
    spaced = '  Flanked by spaces on either side  '  # has leading & trailing spaces
    print('lstrip():', spaced.lstrip())  # removes leading spaces
    print('rstrip():', spaced.rstrip())  # removes trailing spaces
    print('strip():', spaced.strip())  # removes both leading and trailing spaces

    # splitting and partitioning using a custom separator sequence (tabs in example)
    tabbed = 'C:\\t\\tUsers\\t\\tKanetkar\\t\\tDocuments'  # literal \t\t appears
    # split on the literal '\t\t' sequence to recreate chapter example semantics
    parts = tabbed.split('\\t\\t')  # split returns a list of substrings
    print('split on literal \\t\\t ->', parts)
    # partition returns a tuple (before, sep, after) at the first occurrence
    print('partition ->', tabbed.partition('\\t\\t'))


# -----------------------------
# 7. Conversions between numbers and strings
# -----------------------------

def example_str_num_conversions() -> None:
    """Demonstrate str(), int(), float(), complex(), ord() and chr()."""
    print_section('Example: string-number conversions and ord/chr')

    age = 24  # integer value to show conversion
    print('She is ' + str(age) + ' years old')  # str() converts integer to string for concatenation

    # Convert numeric strings back to numbers using int() and float()
    i = int('123')  # convert numeric string to integer
    f = float('3.14')  # convert numeric string to float
    c = complex('2+3j')  # convert numeric string to complex
    print(i, f, c)  # print converted numeric values

    # ord() returns Unicode code point of a single character; chr() reverses it.
    print('ord("A"):', ord('A'))  # prints 65 for 'A'
    print('chr(65):', chr(65))  # prints 'A' given the code point 65


# -----------------------------
# 8. String comparisons (lexicographic) examples
# -----------------------------

def example_comparison() -> None:
    """Show typical string comparison behavior in Python (lexicographic)."""
    print_section('Example: lexicographic string comparisons')

    s1 = 'Bombay'
    s2 = 'bombay'
    s3 = 'Nagpur'
    s4 = 'Bombaywala'
    s5 = 'Bombay'

    # Comparison operators compare strings lexicographically (by character code).
    print('s1 == s2 ->', s1 == s2)  # False: different case
    print('s1 == s5 ->', s1 == s5)  # True: identical content
    print('s1 < s3 ->', s1 < s3)  # True or False depending on lexicographic order
    print('s1 < s2 ->', s1 < s2)  # capitals have smaller code points than lowercase


# -----------------------------
# 9. Problems from the chapter (Problem 4-1 to 4-5)
# -----------------------------

def exercises_chapter_examples() -> None:
    """Solve the chapter problems 4-1 through 4-5 with printed output.

    Each example mirrors the programs and outputs shown in the book.
    """
    print_section('Problem 4-1: demonstrate creation, immutability & built-ins')

    # Simple string
    msg = 'Hoopla'  # store the literal 'Hoopla'
    print(msg)  # print the simple string

    # Strings with special characters and raw variant for paths
    msg2 = 'He said, "Let Us Python"'  # escaped inner quotes
    file1 = 'C:\\temp\\newfile'  # Windows-style path with escaped backslashes
    file2 = r'C:\temp\newfile'  # raw string; preserves the backslashes literally
    print(msg2)
    print(file1)
    print(file2)

    # Multiline strings demonstration
    m1 = 'What is this life if full of care\nWe have no time to stand and stare'
    m2 = ("""What is this life if full of care\n"
           "We have no time to stand and stare""")  # explicit triple-quoted multiline
    m3 = ('What is this life if full of care' ' ' 'We have no time to stand and stare')
    # m3 uses adjacent literal concatenation (no newline between pieces)
    print(m1)
    print(m2)
    print(m3)

    # Replication demonstration
    msg3 = 'Hoopla' * 3  # repetition operator produces repeated string
    print(msg3)

    # Immutability: reassigning works but item assignment doesn't
    s = 'Utopia'  # original name bound to string 'Utopia'
    t = 'Today!!!'  # another string
    s = s + t  # concatenation creates a new string and rebinds s to it
    print(s)

    # Built-in functions len, min and max
    print(len('Hoopla'))  # number of characters
    print(min('Hoopla'))  # smallest character by Unicode
    print(max('Hoopla'))  # largest character by Unicode

    # Problem 4-2: operations on 'Bamboozled'
    print_section("Problem 4-2: string slicing and reversing for 'Bamboozled'")
    s = 'Bamboozled'
    # Various slices to create the outputs requested by the chapter
    print(s[0] + ' ' + s[1])  # 'B a'
    print(s[-2] + ' ' + s[-1])  # 'e d' -> last two characters
    print(s[2:])  # from index 2 to end -> 'mboozled'
    print(s[:6])  # first 6 characters -> 'Bamboo'
    print(s[::-1])  # reverse the string -> 'delzoobmaB'
    # Combine with additions as chapter shows
    s2 = s + 'Hype!'  # append text to s
    print(s2)
    s3 = s[:6] + 'Monger' + s[6:]  # insert 'Monger' into middle
    print(s3)

    # Problem 4-3: content tests on several example strings
    print_section('Problem 4-3: content tests (isalpha, isdigit, isalnum, etc.)')
    s1 = 'NitiAayog'
    s2 = 'And Quiet Flows The Don'
    s3 = '0123456789'  # numeric example (in PDF this was non-ASCII digits)
    s4 = 'Make $$$ a day'  # contains spaces; not purely alphabetic
    print('s1:', s1)
    print('s2:', s2)
    print('s3:', s3)
    print('s4:', s4)
    print('isalpha s1:', s1.isalpha())
    print('isalpha s2:', s2.isalpha())
    print('isdigit s3:', s3.isdigit())
    print('isalnum s1:', s1.isalnum())

    # startswith / endswith example
    print('s2 startswith "And" ->', s2.startswith('And'))
    print('s2 endswith "And" ->', s2.endswith('And'))

    # Problem 4-4: case conversions and trimming
    print_section('Problem 4-4: case conversions, replace & trimming')
    s = 'Bring It On'
    print('upper:', s.upper())
    print('lower:', s.lower())
    print('capitalize:', s.capitalize())
    print('title:', s.title())
    print('swapcase:', s.swapcase())
    # search and replace
    print('find I ->', s.find('I'))
    print('find On ->', s.find('On'))
    print('replace It->Him:', s.replace('It', 'Him'))
    # trimming
    spaced = '  Flanked by spaces on either side  '
    print('lstrip:', spaced.lstrip())
    print('rstrip:', spaced.rstrip())
    print('strip:', spaced.strip())

    # Problem 4-5: find all occurrences of 'T' and replace them with 't'
    print_section("Problem 4-5: finding all 'T' and replacing with 't'")
    s = 'The Terrible Tiger Tore The Towel'
    # Find all positions of 'T' iteratively.
    pos = s.find('T')  # find first 'T'
    while pos != -1:  # loop until find() returns -1 (not found)
        print('Found T at index', pos)
        pos = s.find('T', pos + 1)  # continue searching from next index

    # Replace all 'T' with 't' using replace; count occurrences first.
    count_T = s.count('T')  # how many 'T's occur in the string
    s_replaced = s.replace('T', 't', count_T)  # replace exactly count_T occurrences
    print('Replaced string ->', s_replaced)


# -----------------------------
# 10. End-of-chapter Exercises A & B (Solved)
# -----------------------------

def exercises_A_and_B() -> None:
    """Solve exercises A and B from end of chapter in a compact readable way.

    The function prints answers or code that produces answers. Each
    step includes comments explaining the approach.
    """
    print_section('Exercises: Part A (a to n)')

    # (A)(a) Shenanigan manipulations (similar to Bamboozled exercise)
    s = 'Shenanigan'
    print('Original:', s)  # original string
    # Show "S h" — take first and second character separated by space
    print(s[0] + ' ' + s[1])  # 'S h'
    # "a n" from 2nd and 3rd characters (index 2,3)
    print(s[1] + ' ' + s[2])  # 'h e' or as chapter wants variations; show another slice
    # remainder from index 2 to end
    print(s[2:])  # 'enanigan'
    # prints first 6 characters repeatedly as requested
    print(s[:6])  # 'Shenan'
    print(s[:6])  # printed again to match example outputs
    # full string repeated / combined examples
    print(s)  # the whole string
    # some sample derived strings requested in the chapter (examples)
    print(''.join([s[0], s[2], s[4]]))  # simple sample extraction -> may show 'Sea' etc.
    print(s[0] + s[2] + s[4] + s[6:])  # a different composition

    # (A)(b) Convert the specific sentence to have each word start uppercase
    original = 'Visit ykanetkar]com for online courses in programming'
    # We want to make first letter of every word uppercase but preserve rests.
    words = original.split(' ')  # split into words on spaces
    # Capitalize only the first character of each word, preserve rest exactly.
    words_capitalized = [w[0].upper() + w[1:] if w else w for w in words]
    converted = ' '.join(words_capitalized)
    print('\nOriginal:', original)
    print('Converted:', converted)

    # (A)(c) Convert first and last words in phrase to uppercase, rest unchanged.
    text = ('Light travels faster than sound. This is why some people appear '
            'bright until you hear them speak.')
    # The book's example expects first and last words of the first sentence
    # to become uppercase. We'll split the first sentence and transform it.
    first_sentence, sep, rest = text.partition('.')  # split at first period
    words_fs = first_sentence.split()  # split into words
    # uppercase first and last word of first sentence
    if words_fs:
        words_fs[0] = words_fs[0].upper()  # make first word uppercase
        words_fs[-1] = words_fs[-1].upper()  # make last word uppercase
    transformed_first = ' '.join(words_fs)
    combined = transformed_first + sep + rest  # reassemble the full text
    print('\nOriginal paragraph:\n', text)
    print('\nTransformed paragraph:\n', combined)

    # (A)(d) Predict output of given snippet with 'HumptyDumpty'
    s = 'HumptyDumpty'
    print('\nSnippet results for s = "HumptyDumpty"')
    print(s == s)  # boolean equality with itself -> True
    print(s.isalpha())  # True (only alphabets present)
    print(s.isdigit())  # False (not numeric)
    print(s.isalnum())  # True (alphabetic, so also alnum)
    print(s.islower())  # False (not all lowercase)
    print(s.isupper())  # False (not all uppercase)
    print(s.startswith('Hump'))  # True if starts with 'Hump'
    print(s.endswith('Dump'))  # False ('HumptyDumpty' ends with 'pty')

    # (A)(e) Purpose of a raw string — print a concise explanation.
    print('\nPurpose of raw string:')
    print('A raw string (prefix r) tells Python not to treat backslashes as escapes;')
    print('this is useful for windows paths and regular expressions where backslashes')
    print('should be preserved verbatim.')

    # (A)(f) Working with individual words = use split()
    sample = ('The difference between stupidity and genius is that genius '
              'has its limits')
    words = sample.split()  # default split on whitespace produces list of words
    print('\nWords extracted from sample (first 8 shown):', words[:8])

    # (A)(g) Two ways to store the string He said, "Let Us Python"
    # 1) Escape inner quotes
    a1 = 'He said, "Let Us Python"'
    # 2) Use opposite outer quotes to avoid escapes
    a2 = "He said, 'Let Us Python'"
    print('\nTwo storage styles:')
    print(a1)
    print(a2)

    # (A)(h) id and type of 'Imaginary'
    print('\nID and type of literal "Imaginary":')
    print('id("Imaginary") ->', id('Imaginary'))
    print('type("Imaginary") ->', type('Imaginary'))

    # (A)(i) Splitting the tabbed path literal used earlier
    s_tab = 'C:\\t\\tUsers\\t\\tKanetkar\\t\\tDocuments'
    print('\nsplit on "\\t\\t" ->', s_tab.split('\\t\\t'))
    print('partition on "\\t\\t" ->', s_tab.partition('\\t\\t'))

    # (A)(j) Strings are iterable, sliceable and immutable -> True
    print('\nStrings are iterable, sliceable and immutable ->', True)

    # (A)(k) Extract 'TraPoete' from 'ThreadProperties' by taking even indices
    s_tp = 'ThreadProperties'
    extracted = s_tp[0::2]  # take characters at indices 0,2,4,... -> 'TraPoete'
    print('\nExtracted from ThreadProperties ->', extracted)

    # (A)(l) Eliminate spaces on either side -> use strip()
    flanked = '  Flanked by spaces on either side  '
    print('After strip() ->', flanked.strip())

    # (A)(m) Show ids for three related string variables
    s1 = 'Hello'
    s2 = s1  # s2 references the same object as s1
    s3 = s1 + ''  # concatenation with empty string usually creates a new object
    print('\nIDs of s1, s2 and s3 ->', id(s1), id(s2), id(s3))

    # (A)(n) Last character extracted using negative index
    msg = 'Aeroplane'
    ch = msg[-1]  # -1 indexes the last character in a Python sequence
    print('\nLast character of "Aeroplane" ->', ch)

    # -------------------------
    # Part B: matching pairs — demonstrate results for each item
    # -------------------------
    print_section('Exercises: Part B (matching pairs demonstration)')
    msg = 'Keep yourself warm'
    print('msg ->', msg)

    # a) msg.partition(' ') -> tuple (before, sep, after)
    a = msg.partition(' ')
    print('a) partition ->', a)

    # b) msg.split(' ') -> list of words (split on spaces)
    b = msg.split(' ')
    print('b) split ->', b)

    # c) msg.startswith('Keep') -> boolean True if msg begins with Keep
    c = msg.startswith('Keep')
    print("c) startswith('Keep') ->", c)

    # d) msg.endswith('Keep') -> boolean (should be False here)
    d = msg.endswith('Keep')
    print("d) endswith('Keep') ->", d)

    # e) msg.swapcase() -> swap the case of every character
    e = msg.swapcase()
    print('e) swapcase ->', e)

    # f) msg.capitalize() -> capitalise the first character of the string
    f = msg.capitalize()
    print('f) capitalize ->', f)

    # g) msg.count('e') -> number of occurrences of 'e'
    g = msg.count('e')
    print("g) count('e') ->", g)

    # h) len(msg) -> length of the message
    h = len(msg)
    print('h) len(msg) ->', h)

    # i) msg[0:11] -> substring from start up to index 11 (exclusive)
    i = msg[0:11]
    print('i) msg[0:11] ->', i)

    # j) msg[2:len(msg)-2] -> a long slice example
    j = msg[2:len(msg)-2]
    print('j) example slice ->', j)

    # k) msg[0] -> first character
    k = msg[0]
    print('k) first character ->', k)

    # l) msg[2:5] -> small slice; example placeholder
    l = msg[2:5]
    print('l) slice(2,5) ->', l)

    # m) msg[12:15] -> small slice near the end (may be empty if out of range)
    m = msg[12:15]
    print('m) slice around end ->', m)

    # n) msg[4:7] -> another slice (example)
    n = msg[4:7]
    print('n) slice(4,7) ->', n)

    # o) msg[0:0] -> empty string as a slice example
    o = msg[0:0]
    print('o) empty slice ->', repr(o))


# -----------------------------
# If this file is executed directly, run all examples in sequence.
# -----------------------------

if __name__ == '__main__':
    # Calling each example function prints both demonstration code and
    # the results, so the script is self-explanatory when executed.
    example_simple_strings()
    example_indexing_slicing()
    example_immutability_concat_membership()
    example_builtins_type_id()
    example_string_methods()
    example_conversions_search_trim_split()
    example_str_num_conversions()
    example_comparison()
    exercises_chapter_examples()
    exercises_A_and_B()

    # final marker for script termination
    print('\nAll examples and exercises from Chapter 4 have finished running.')
