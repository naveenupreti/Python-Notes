# ======================================================
# DOS Emulator in Python
# Supports 'type' and 'copy' commands
# ======================================================

import os

def type_file(filename):
    """Emulate 'type' command: display file content"""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return
    with open(filename, 'r') as f:
        print(f.read())

def copy_file(source, destination):
    """Emulate 'copy' command: copy source to destination"""
    if not os.path.exists(source):
        print(f"Error: Source file '{source}' does not exist.")
        return
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())
    print(f"Copied '{source}' to '{destination}'.")

# ------------------------------------------------------
# Interactive loop
# ------------------------------------------------------
print("DOS Emulator (type 'exit' to quit)")
while True:
    cmd_input = input("C:\\> ").strip()
    if cmd_input.lower() == "exit":
        print("Exiting DOS Emulator...")
        break
    if not cmd_input:
        continue
    
    parts = cmd_input.split()
    command = parts[0].lower()

    if command == "type":
        if len(parts) != 2:
            print("Usage: type <filename>")
            continue
        type_file(parts[1])
    
    elif command == "copy":
        if len(parts) != 3:
            print("Usage: copy <source> <destination>")
            continue
        copy_file(parts[1], parts[2])
    
    else:
        print("Unknown command. Use 'type', 'copy', or 'exit'.")
