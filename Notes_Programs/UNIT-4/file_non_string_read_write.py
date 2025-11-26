'''
Reading & Writing Non-String Data in Python

When working with files, the write() and read() functions accept only strings.
But we often need to store lists, dictionaries, numbers, sets, objects, or binary data.

Python provides following methods to store non-string data:

1. Using str() and eval()
✔ Purpose

Convert Python objects into a string, save the string, and convert back later.

✔ When to Use

For small/simple data (lists, tuples, dicts) when security is not a concern.
'''
#Example
data_list = [10, 20, 30]

# Convert list → string and write to file
with open("list.txt", "w") as f:
    f.write(str(data_list))

# Read string and convert back to list
with open("list.txt", "r") as f:
    content = f.read()

restored_list = eval(content)
print(restored_list)

'''
🧠 Functions used
str(object)

Converts any Python object into its string representation.

Example:
str([1,2,3]) ⇒ "[1, 2, 3]"

eval(string)

Evaluates a Python expression from a string and returns the object.

Example:
eval("[1,2,3]") ⇒ [1, 2, 3]

⚠ Not safe for untrusted files.
If the file contains malicious code, eval() will execute it.

2. Using the json Module
✔ Purpose

Save data in structured, human-readable, language-independent format.

✔ Best For

Dicts, lists, numbers, strings — GREAT for config files & web data.

If your data is JSON-compatible:
    ✔ dict
    ✔ list
    ✔ int
    ✔ float
    ✔ str
    ✔ bool
    ✔ None

Then JSON is the most secure method.

Why secure?

    JSON loads only data types (never executes code)

    Cannot contain code instructions

    Immune to code injection

    Supported across all languages

But JSON cannot store:

    sets

    tuples

    custom classes

    Python-only objects

🥈 2. Custom Serialization (Safest for Complex Data)

If you need to store any object, you should manually convert it into a safe format.

    Example:

    Convert:

    sets → lists

    tuples → lists

    objects → dictionaries
'''
#Example
import json

student = {"name": "Naveen", "marks": [91, 82, 87]}

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

with open("student.json", "r") as f:
    restored_json = json.load(f)

print(restored_json)

'''
🧠 Functions used
json.dump(obj, file, indent=4)

Writes Python object to a file in JSON format.
indent=4 gives pretty formatting.

Example output:

{
    "name": "Naveen",
    "marks": [91, 82, 87]
}

json.load(file)

Reads JSON from a file and converts it back to Python object (dict/list).

JSON Limitations

❌ Cannot store:

sets

tuples

custom objects

✅ Serialization
Definition:
Serialization is the process of converting a Python object into a format that can be:
    stored in a file
    saved in a database
    sent over a network
    converted to JSON / bytes

Why do we need it?
Because Python objects (like class objects) cannot be directly saved or transferred.
They must be converted to a storable format like:
    JSON
    Pickle bytes
    XML
    Binary format

Simple Example
import json

data = {"name": "Aman", "marks": 90}

json_string = json.dumps(data)
print(json_string)

Output:

{"name": "Aman", "marks": 90}

You converted a Python dictionary → JSON string.

This is serialization.

✅ Deserialization
Definition:
Deserialization is the reverse process:
Converting the stored data back into a Python object.

Example
import json

json_string = '{"name": "Aman", "marks": 90}'
data = json.loads(json_string)

print(data)
print(data["name"])

Output:

{'name': 'Aman', 'marks': 90}
Aman

You converted JSON → Python dictionary.

This is deserialization.

🔁 Serialization vs Deserialization (Simple Table)
Concept					Meaning								Example
Serialization		Python object → storable format		dict → JSON
Deserialization		stored format → Python object		JSON → dict


📌 3. Using the pickle Module
✔ Purpose

Store ANY Python object in binary format.

✔ Best For

Sets, tuples, custom classes, complex data structures.
'''
#Example
import pickle

my_set = {2, 4, 6, 8}

with open("set.pkl", "wb") as f:
    pickle.dump(my_set, f)

with open("set.pkl", "rb") as f:
    restored_pickle = pickle.load(f)

print(restored_pickle)

'''
🧠 Functions used
pickle.dump(obj, file)

Serializes any Python object into binary and writes to file.

pickle.load(file)

Reads binary data and reconstructs the original Python object.

⚠ Important

Pickle is not secure if file comes from an unknown or unsafe source.
'''
