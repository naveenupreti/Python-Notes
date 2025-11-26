'''
1. How Floats Are Stored in Memory (IEEE-754)

Python’s float is stored internally using the IEEE-754 standard.
This is the same standard used in C, Java, CPUs, and GPUs.

✅ IEEE-754 Format (32-bit Float)

A 32-bit float (also called single precision) uses:

Field	Bits	Purpose
Sign bit	1	0 = positive, 1 = negative
Exponent	8	Stores magnitude (using bias 127)
Fraction / Mantissa	23	Stores decimal precision

Total = 1 + 8 + 23 = 32 bits

🧠 Example: How is 3.14 stored?

Let's break down:

3.14 (decimal)

Step 1 — Convert to binary

3.14 ≈ 11.00100011110101110000101₂

Step 2 — Normalize

Move decimal to get 1.xxxx × 2ⁿ

11.001000...  = 1.1001000... × 2¹


So:

Exponent = 1

Mantissa = 1001000...

Step 3 — Apply exponent bias

IEEE-754 exponent uses bias 127:

Stored exponent = 1 + 127 = 128
Binary = 10000000

Step 4 — Final IEEE-754 structure for 3.14
Sign	Exponent	Mantissa
0	10000000	10010001111010111000011

Convert to hex:

0x4048F5C3


In memory it is stored as 4 bytes:

40 48 F5 C3

🧪 Verify in Python
import struct

print(struct.pack("f", 3.14))


Output:

b'\xc3\xf5H@'


This is little-endian byte order:

c3 f5 48 40

🏆 Summary of IEEE-754 Float Storage

A float is NOT stored as decimal.

It is stored in binary, split into:

Sign (1 bit)

Exponent (8 bits)

Mantissa (23 bits)

This binary representation is what struct.pack() produces.

🪄 2. How to Unpack This Data Back to Python Objects

If you used:

data = struct.pack("if", 10, 3.14)


Then data contains 8 bytes:

[integer][float]
4 bytes | 4 bytes


To convert back:

✔ Unpacking using struct.unpack()
import struct

data = struct.pack("if", 10, 3.14)

value = struct.unpack("if", data)
print(value)


Output:

(10, 3.140000104904175)

Why slight difference?

Because binary floats cannot store 3.14 exactly, they store the nearest representable value.

🧩 Meaning of the Result

struct.unpack():

reads the binary bytes

interprets first 4 bytes as i

interprets next 4 bytes as f

returns a tuple of Python values

🔍 To inspect raw bytes
print(list(data))


Example output:

[10, 0, 0, 0, 195, 245, 72, 64]

🧠 Recap
IEEE-754 float storage:

3.14 → binary fraction → sign + exponent + mantissa

stored as 4 bytes: c3 f5 48 40

Packing/unpacking:

struct.pack("if", 10, 3.14) → convert values → binary

struct.unpack("if", data) → convert binary → Python values

📌 4. Using the struct Module
✔ Purpose
Pack and unpack numbers into compact binary format, similar to C structs.

✔ Best For
    Low-level binary files
    Embedded systems
    Scientific/sensor data
    Exchanging data with C/C++ programs
'''
#Example
import struct

# pack integer + float into binary
with open("binary.bin", "wb") as f:
    f.write(struct.pack("if", 100, 3.14))

with open("binary.bin", "rb") as f:
    data = f.read()

num, fl = struct.unpack("if", data)
print(num, fl)

'''
🧠 Functions used
struct.pack(format, values...)

Converts numbers into binary bytes.

Format codes:

"i" → integer (4 bytes)

"f" → float (4 bytes)

"d" → double (8 bytes)

Example:
struct.pack("if", 10, 3.14) produces 8 bytes of binary data.

struct.unpack(format, byte_data)

Converts binary bytes back into numbers.

Example:
struct.unpack("if", data) ⇒ (10, 3.14)

✅ 1. What is struct.pack()?

struct is a Python module that converts Python values → binary data (bytes).

pack() takes:

format string (like "if")

values to pack

✅ 2. Understanding the Format String "if"

The format string tells Python what data types to pack and how many bytes each should take.

Code	Meaning	Size in bytes
i	integer (32-bit signed)	4 bytes
f	float (32-bit, single precision)	4 bytes

So "if" means:

i → 4 bytes
f → 4 bytes
Total = 8 bytes

🔍 3. Packing the Data
struct.pack("if", 10, 3.14)


This does two things:

✔ Packs the integer 10

Stored in 4 bytes (32 bits)

Binary form of 10 is:
00000000 00000000 00000000 00001010

✔ Packs the float 3.14

Also stored in 4 bytes

But floats are stored in IEEE-754 binary format,
so its binary representation is something like:
@H\xf5\xc3 (raw binary)

🧪 4. Verify the size (try this in Python)
import struct

data = struct.pack("if", 10, 3.14)
print(data)
print(len(data))   # prints 8


Output:

b'\n\x00\x00\x00\xc3\xf5H@'
8

🧠 Why does it produce 8 bytes?

Because:

i → integer → 4 bytes

f → float → 4 bytes

Total:

4 + 4 = 8 bytes

📝 Summary

struct.pack("if", 10, 3.14)
→ converts the values into binary format using the layout specified in "if"
→ integer + float
→ 8 bytes total
'''