# -------------------------------------------------------------
# Program: Copy a Binary File (like image, audio, video, pdf...)
# Purpose: Demonstrates how to handle binary files in Python
# Usage:   python3 file_copy_binary_cla.py source_file destination_file
# -------------------------------------------------------------

import sys   # sys module lets us access command line arguments

# --------------------
# Command Line Arguments
# --------------------
# sys.argv is a list of command line arguments:
#   sys.argv[0] → script name (file_copy_binary_cla.py)
#   sys.argv[1] → source file name
#   sys.argv[2] → destination file name
# We check if the user provided exactly 2 arguments (source + destination).
if len(sys.argv) != 3:
    print("❌ Usage: python3 file_copy_binary_cla.py <source_file> <destination_file>")
    sys.exit(1)   # Exit program with error code 1

# Assign arguments to variables
source = sys.argv[1]        # The file to be copied
destination = sys.argv[2]   # The new file name

try:
    # Open the source file in binary read mode ('rb')
    # Required for non-text files like images/videos
    with open(source, 'rb') as f_src:

        # Open the destination file in binary write mode ('wb')
        # Creates the file if it doesn't exist
        with open(destination, 'wb') as f_dest:

            # Read and write in small chunks (4 KB at a time)
            # Efficient for copying large files
            while True:
                chunk = f_src.read(4096)   # Read 4096 bytes (4 KB)
                if not chunk:             # If no more data → stop
                    break
                f_dest.write(chunk)       # Write the chunk to new file

    print(f"✔ File copied successfully to '{destination}'")

# --------------------
# Error Handling
# --------------------
except FileNotFoundError:
    print("❌ Error: The source file does not exist.")

except PermissionError:
    print("❌ Error: You don't have access to this file.")

except Exception as e:
    print("❌ An unexpected error occurred:", e)
