# -------------------------------------------------------------
# Program: Copy a Binary File (like image, audio, video, pdf...)
# Purpose: Demonstrates how to handle binary files in Python
# -------------------------------------------------------------

# Ask the user for the source file name (the file to be copied)
source = input("Enter the source binary file name (example: photo.jpg): ")

# Ask the user for the destination file name (the new file)
destination = input("Enter the destination file name (example: photo_copy.jpg): ")

try:
    # Open the source file in binary read mode ('rb')
    # This is required for non-text files like images/videos
    with open(source, 'rb') as f_src:

        # Open the destination file in binary write mode ('wb')
        # This will create the file if it doesn't exist
        with open(destination, 'wb') as f_dest:

            # Read and write in small chunks (4 KB at a time)
            # This is efficient for copying large files (even GBs)
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
