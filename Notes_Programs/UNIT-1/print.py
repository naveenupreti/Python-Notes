# ============================================================
# SECTION 0: Print Function Demonstration
# ============================================================

print("\n--- SECTION 0: Print Function ---")

import sys
import time

# 1. Default print behavior
print("Hello", "World")  # prints with default space separator and newline

# 2. Using sep to change separator
print("Hello", "World", sep="---")  # Hello---World

# 3. Using end to change line ending
print("Hello", end="!")  # Output stays on the same line
print("World")           # World prints immediately after !

# 4. Using file to redirect output to a file
with open("print_demo.txt", "w") as f:
    print("Hello File", file=f)

# 5. Using flush to force immediate output
print("Counting:", end=' ', flush=True)
for i in range(1, 6):
    print(i, end=' ', flush=True)  # ensures each number prints immediately
    time.sleep(0.5)
print()  # newline after counting

# Explanation:
# sep -> separates multiple objects (default ' ')
# end -> string appended at the end (default '\n')
# file -> where to print (default sys.stdout, i.e., console)
# flush -> True forces immediate writing, False allows buffering
