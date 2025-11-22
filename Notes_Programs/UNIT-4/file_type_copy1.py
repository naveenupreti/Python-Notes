# ======================================================
# DOS Emulator in Python: 'type' and 'copy' commands
# ======================================================

import os

def type_file(filename):
    """
    Emulate DOS 'type' command: Display contents of a file
    """
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Contents of '{filename}':\n")
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

def copy_file(source, destination):
    """
    Emulate DOS 'copy' command: Copy contents from source to destination
    """
    if not os.path.exists(source):
        print(f"Error: Source file '{source}' does not exist.")
        return
    try:
        with open(source, 'r') as src:
            data = src.read()
        with open(destination, 'w') as dest:
            dest.write(data)
        print(f"Copied content from '{source}' to '{destination}'.")
    except Exception as e:
        print(f"Error copying file: {e}")

# ----------------------------
# Main program
# ----------------------------
def main():
    print("DOS Emulator - Python Version")
    print("Commands available:")
    print("1. type <filename>")
    print("2. copy <source> <destination>")
    print("3. exit")
    
    while True:
        cmd = input("\nEnter command: ").strip()
        if cmd.lower() == "exit":
            print("Exiting DOS Emulator...")
            break
        parts = cmd.split()
        if len(parts) == 0:
            continue
        
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
            print("Unknown command. Try 'type', 'copy', or 'exit'.")

# Run the main program
if __name__ == "__main__":
    main()
