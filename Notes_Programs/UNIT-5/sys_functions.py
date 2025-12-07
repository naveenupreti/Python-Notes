'''
sys

Purpose:
Used to interact with Python interpreter and system.

Important Attributes/Functions:
| Function/Attribute | Description               | Example                  |
| ------------------ | ------------------------- | ------------------------ |
| `sys.argv`         | List of command-line args | `sys.argv[0]`            |
| `sys.version`      | Python version            | `print(sys.version)`     |
| `sys.path`         | Module search paths       | `print(sys.path)`        |
| `sys.exit()`       | Exit program              | `sys.exit()`             |
| `sys.maxsize`      | Maximum integer           | `print(sys.maxsize)`     |
| `sys.getsizeof()`  | Memory size of object     | `sys.getsizeof([1,2,3])` |
| `sys.platform`     | OS platform               | `sys.platform`           |

'''
# -------------------------------------------------------------
# Program: Important sys module functions + OUTPUT
# -------------------------------------------------------------
import sys

# argv – list of command-line arguments
# NOTE: When running normally, argv will only contain the script name.
print("sys.argv:", sys.argv)

# version – Python version
print("\nPython version:", sys.version)

# path – list of directories where Python searches modules
print("\nPython module search paths:")
for p in sys.path:
    print(p)

# getsizeof() – memory size of an object in bytes
x = [1, 2, 3, 4]
print("\nSize of list x:", sys.getsizeof(x), "bytes")

# exit() – terminate program (won’t use here, just showing syntax)
# sys.exit()

# maxsize – largest integer Python can handle
print("\nMax integer size:", sys.maxsize)

# platform – OS information
print("\nPlatform:", sys.platform)


# -------------------------------------------------------------
# SAMPLE OUTPUT (Will vary depending on system)
# -------------------------------------------------------------
"""
sys.argv: ['sys_functions.py']

Python version: 3.10.12 (tags/v3.10.12:3d1f4e4, Jun  6 2023, 23:15:00)

Python module search paths:
C:\Python310\python310.zip
C:\Python310\DLLs
C:\Python310\lib
...

Size of list x: 88 bytes

Max integer size: 9223372036854775807

Platform: win32
"""
