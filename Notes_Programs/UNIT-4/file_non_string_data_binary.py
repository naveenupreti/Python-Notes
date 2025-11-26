import struct   # Used for packing and unpacking numbers

# -------------------------------
# Writing non-string data (binary)
# -------------------------------
with open("data.bin", "wb") as f:

    # 1. Write raw bytes
    f.write(b"ABC")   # 3 bytes: 41 42 43 in hex

    # 2. Write a few integers as bytes
    f.write(bytearray([10, 20, 30]))  # 3 bytes

    # 3. Write an integer + float using struct.pack
    packed_data = struct.pack("if", 100, 3.14)
    f.write(packed_data)  # 8 bytes


# -------------------------------
# Reading back the binary data
# -------------------------------
with open("data.bin", "rb") as f:

    # Read first 3 bytes ("ABC")
    raw1 = f.read(3)
    print("Raw bytes:", raw1)

    # Read next 3 bytes (10, 20, 30)
    raw2 = f.read(3)
    print("Bytearray values:", list(raw2))

    # Read next 8 bytes (int + float)
    raw3 = f.read(8)

    # Unpack: "i" = int, "f" = float
    number, decimal = struct.unpack("if", raw3)
    print("Unpacked integer:", number)
    print("Unpacked float:", decimal)
