'''
Regular Expression - Regex (re module)

Purpose:
Used for pattern matching, searching, and text manipulation.

Important Functions:
| Function        | Description                 | Example                                 |
| --------------- | --------------------------- | --------------------------------------- |
| `re.search()`   | Search first match anywhere | `re.search(r'\d+', 'abc123')`           |
| `re.match()`    | Match from beginning        | `re.match(r'\d+', '123abc')`            |
| `re.findall()`  | Return all matches          | `re.findall(r'\d+', '12 34')`           |
| `re.finditer()` | Iterator over match objects | `for m in re.finditer(r'\d+', '12 34')` |
| `re.sub()`      | Replace matched text        | `re.sub(r'\d', '#', 'a1b2')`            |
| `re.split()`    | Split string using regex    | `re.split(r'\s+', 'Hello World')`       |
| `re.compile()`  | Compile pattern for reuse   | `p = re.compile(r'\d+')`                |

'''
# -------------------------------------------------------------
# Important regex functions with inline comments + OUTPUT
# -------------------------------------------------------------
import re

text = "Hello 123 world 4567. Contact: abc@test.com"

m = re.search(r"\d+", text)
print("search() result:", m.group())

m2 = re.match(r"\d+", text)
print("match() result:", m2)

print("\nfindall():", re.findall(r"\d+", text))

print("\nfinditer():")
for match in re.finditer(r"\d+", text):
    print("Match:", match.group(), "Span:", match.span())

print("\nsub():", re.sub(r"\d", "#", text))
print("split():", re.split(r"\s+", text))

m3 = re.search("world", text)
print("\nMatched:", m3.group())
print("Start:", m3.start())
print("End:", m3.end())
print("Span:", m3.span())

pattern = re.compile(r"[a-zA-Z]+")
print("\nWords using compiled pattern:", pattern.findall(text))


# -------------------------------------------------------------
# SAMPLE OUTPUT
# -------------------------------------------------------------
"""
search() result: 123
match() result: None

findall(): ['123', '4567']

finditer():
Match: 123 Span: (6, 9)
Match: 4567 Span: (16, 20)

sub(): Hello ### world ####. Contact: abc@test.com
split(): ['Hello', '123', 'world', '4567.', 'Contact:', 'abc@test.com']

Matched: world
Start: 10
End: 15
Span: (10, 15)

Words using compiled pattern:
['Hello', 'world', 'Contact', 'abc', 'test', 'com']
"""
