# ======================================================================
#                 FILE MODES IN PYTHON
# ======================================================================
# Python allows combining:
#   Basic modes : r, w, a, x
#   Type modes  : t (text), b (binary)
#   Modifier    : + (read + write)
#
# This script contains a practical demonstration of ALL valid modes.
# ======================================================================
'''
| Mode | Meaning / Purpose                            | Creates File? | Cursor Position | Text/Binary |
| ---- | -------------------------------------------- | ------------- | --------------- | ----------- |
| r    | Read (text)                                  | No            | Beginning       | Text        |
| w    | Write (text) – overwrites                    | Yes           | Beginning       | Text        |
| a    | Append (text)                                | Yes           | End             | Text        |
| r+   | Read + write (text)                          | No            | Beginning       | Text        |
| w+   | Write + read (text) – overwrites             | Yes           | Beginning       | Text        |
| a+   | Append + read (text)                         | Yes           | End             | Text        |
| b    | Binary mode modifier (used with other modes) | -             | -               | Binary      |
| rb   | Read (binary)                                | No            | Beginning       | Binary      |
| wb   | Write (binary) – overwrites                  | Yes           | Beginning       | Binary      |
| ab   | Append (binary)                              | Yes           | End             | Binary      |
| r+b  | Read + write (binary)                        | No            | Beginning       | Binary      |
| w+b  | Write + read (binary) – overwrites           | Yes           | Beginning       | Binary      |
| a+b  | Append + read (binary)                       | Yes           | End             | Binary      |
| x    | Exclusive write (fails if file exists, text) | Yes           | Beginning       | Text        |
| xb   | Exclusive write (binary)                     | Yes           | Beginning       | Binary      |
| x+   | Exclusive write + read (text)                | Yes           | Beginning       | Text        |
| x+b  | Exclusive write + read (binary)              | Yes           | Beginning       | Binary      |

'''
# --------------------------------------------------------------
# MODE: 'r'  → READ ONLY (file must exist)
# --------------------------------------------------------------
with open("demo_r.txt", "w") as f:
    f.write("Content for r mode.\n")

print("\n--- MODE: r (read only) ---")
with open("demo_r.txt", "r") as f:
    print(f.read())  # simply reads file


# --------------------------------------------------------------
# MODE: 'w' → WRITE ONLY (creates / overwrites)
# --------------------------------------------------------------
print("\n--- MODE: w (write only, overwrites) ---")
with open("demo_w.txt", "w") as f:
    f.write("Created using w mode.\n")
print("demo_w.txt created and overwritten.")


# --------------------------------------------------------------
# MODE: 'a' → APPEND ONLY (creates if missing)
# --------------------------------------------------------------
print("\n--- MODE: a (append only) ---")
with open("demo_a.txt", "a") as f:
    f.write("Appended line (a mode).\n")
print("demo_a.txt appended.")


# --------------------------------------------------------------
# MODE: 'x' → EXCLUSIVE CREATE (error if file exists)
# --------------------------------------------------------------
print("\n--- MODE: x (exclusive create) ---")

try:
    with open("demo_x.txt", "x") as f:
        f.write("Created only once using x mode.\n")
    print("demo_x.txt created successfully.")
except FileExistsError:
    print("demo_x.txt already exists (x mode prevents overwrite).")


# --------------------------------------------------------------
# MODE: 'r+' → READ + WRITE (file must exist)
# --------------------------------------------------------------
print("\n--- MODE: r+ (read + write, no creation) ---")
with open("demo_r_plus.txt", "w") as f:
    f.write("Initial content for r+.\n")

with open("demo_r_plus.txt", "r+") as f:
    print("Before writing:", f.read())
    f.seek(0)
    f.write("UPDATED using r+.\n")  # overwrites beginning


# --------------------------------------------------------------
# MODE: 'w+' → WRITE + READ (overwrites or creates)
# --------------------------------------------------------------
print("\n--- MODE: w+ (write + read) ---")
with open("demo_w_plus.txt", "w+") as f:
    f.write("Written using w+.\n")
    f.seek(0)
    print(f.read())  # now read it back


# --------------------------------------------------------------
# MODE: 'a+' → APPEND + READ (creates if missing)
# --------------------------------------------------------------
print("\n--- MODE: a+ (append + read) ---")
with open("demo_a_plus.txt", "a+") as f:
    f.write("Appended using a+.\n")
    f.seek(0)
    print(f.read())  # read entire file


# --------------------------------------------------------------
# MODE: 'x+' → EXCLUSIVE CREATE + READ/WRITE
# --------------------------------------------------------------
print("\n--- MODE: x+ (exclusive create + read/write) ---")
try:
    with open("demo_x_plus.txt", "x+") as f:
        f.write("Created once using x+.\n")
        f.seek(0)
        print(f.read())
except FileExistsError:
    print("demo_x_plus.txt already exists.")


# --------------------------------------------------------------
# BINARY MODES (rb, wb, ab, xb)
# --------------------------------------------------------------
print("\n--- BINARY MODES ---")

# Prepare binary file
with open("binary_sample.bin", "wb") as f:
    f.write(b"BinaryData123")

# rb → read binary
with open("binary_sample.bin", "rb") as f:
    print("rb read:", f.read())

# wb → write binary (overwrites)
with open("binary_w.bin", "wb") as f:
    f.write(b"Written using wb mode.")

# ab → append binary
with open("binary_a.bin", "ab") as f:
    f.write(b"AppendedData")

# xb → exclusive create binary
try:
    with open("binary_x.bin", "xb") as f:
        f.write(b"Created using xb mode.")
    print("binary_x.bin created.")
except FileExistsError:
    print("binary_x.bin already exists.")


# --------------------------------------------------------------
# BINARY READ+WRITE MODES (r+b, w+b, a+b, x+b)
# --------------------------------------------------------------
print("\n--- BINARY READ + WRITE MODES ---")

# r+b → file must exist
with open("binary_sample.bin", "r+b") as f:
    f.seek(0)
    print("r+b reading:", f.read())

# w+b → overwrite + read
with open("binary_w_plus.bin", "w+b") as f:
    f.write(b"Data for w+b.")
    f.seek(0)
    print("w+b reading:", f.read())

# a+b → append + read
with open("binary_a_plus.bin", "a+b") as f:
    f.write(b"Append_for_a+b")
    f.seek(0)
    print("a+b reading:", f.read())

# x+b → exclusive create + read/write
try:
    with open("binary_x_plus.bin", "x+b") as f:
        f.write(b"Created once using x+b.")
        f.seek(0)
        print("x+b reading:", f.read())
except FileExistsError:
    print("binary_x_plus.bin already exists.")


# --------------------------------------------------------------
# TEXT MODE SUFFIXES (rt, wt, xt, at)
# NOTE: 't' is default, so rt == r, wt == w, etc.
# --------------------------------------------------------------
print("\n--- TEXT SUFFIX MODES (rt, wt, at, xt) ---")

with open("text_rt.txt", "rt") as f:
    print("rt == r mode (read text)")

with open("text_wt.txt", "wt") as f:
    f.write("wt == w but text mode explicitly.")

with open("text_at.txt", "at") as f:
    f.write("This is at mode.\n")

try:
    with open("text_xt.txt", "xt") as f:
        f.write("xt == x but text mode.")
        print("xt created.")
except FileExistsError:
    print("text_xt.txt exists.")


# --------------------------------------------------------------
# ALL READ+WRITE TEXT MODES (r+t, w+t, a+t, x+t)
# --------------------------------------------------------------
print("\n--- READ+WRITE TEXT MODES (r+t, w+t, a+t, x+t) ---")

# r+t → read & write text (file must exist)
with open("mode_r_plus_txt.txt", "w") as f:
    f.write("Hello r+t")

with open("mode_r_plus_txt.txt", "r+t") as f:
    print("r+t read:", f.read())

# w+t → overwrite + read text
with open("mode_w_plus_txt.txt", "w+t") as f:
    f.write("Hello w+t")
    f.seek(0)
    print("w+t read:", f.read())

# a+t → append + read text
with open("mode_a_plus_txt.txt", "a+t") as f:
    f.write("Hello a+t\n")
    f.seek(0)
    print("a+t read:", f.read())

# x+t → create + read/write text
try:
    with open("mode_x_plus_txt.txt", "x+t") as f:
        f.write("Hello x+t")
        f.seek(0)
        print("x+t read:", f.read())
except FileExistsError:
    print("mode_x_plus_txt exists already.")

# ======================================================================
# END OF SCRIPT — ALL VALID MODES IN PYTHON 3.11 DEMONSTRATED
# ======================================================================

