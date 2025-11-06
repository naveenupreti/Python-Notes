# ============================================================
# Program: List Operations Demonstration
# Purpose: To show various operations (concatenation, aliasing, etc.)
# ============================================================

print("=== OPERATIONS ON LISTS ===")

# Create two sample lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Original lists:")
print("list1 =", list1)
print("list2 =", list2)

# --- 1️⃣ Concatenation ---
print("\n1️⃣ Concatenation (+ operator)")
result = list1 + list2
print("list1 + list2 =", result)  # [1, 2, 3, 4, 5, 6]
print("✅ Concatenation works with lists")

# --- 2️⃣ Merging ---
print("\n2️⃣ Merging")
print("# Merging is same as concatenation or using extend()")
merged = list1.copy()
merged.extend(list2)
print("After extend():", merged)  # [1, 2, 3, 4, 5, 6]
print("✅ Merging works on lists")

# --- 3️⃣ Conversion ---
print("\n3️⃣ Conversion Works")
print("# Lists can be converted to tuple or set easily")
print("tuple(list1) ->", tuple(list1))
print("set(list1)   ->", set(list1))
print("✅ Conversion between data types works")

# --- 4️⃣ Aliasing ---
print("\n4️⃣ Aliasing (Two names for same list)")
alias = list1
alias.append(99)
print("alias:", alias)
print("list1:", list1)
print("✅ Aliasing works — both refer to same object")

# --- 5️⃣ Cloning ---
print("\n5️⃣ Cloning (Independent copy)")
clone = list1.copy()
clone.append(100)
print("clone:", clone)
print("list1:", list1)
print("✅ Cloning works — independent copy created")

# --- 6️⃣ Searching ---
print("\n6️⃣ Searching Elements")
print("2 in list1 ->", 2 in list1)
print("10 in list1 ->", 10 in list1)
print("✅ Searching using 'in' works fine")

# --- 7️⃣ Identity ---
print("\n7️⃣ Identity")
print("list1 is alias ->", list1 is alias)
print("list1 is clone ->", list1 is clone)
print("✅ Identity check works using 'is'")

# --- 8️⃣ Comparison ---
print("\n8️⃣ Comparison")
print("[1, 2, 3] == [1, 2, 3] ->", [1, 2, 3] == [1, 2, 3])
print("[1, 2, 3] < [2, 0, 0] ->", [1, 2, 3] < [2, 0, 0])
print("✅ Comparison (<, >, ==) works for lists")

# --- 9️⃣ Emptiness ---
print("\n9️⃣ Emptiness Check")
empty_list = []
print("not empty_list ->", not empty_list)
print("not list1 ->", not list1)
print("✅ Emptiness check works using 'not list'")

# --- Summary ---
print("\n" + "="*70)
print("🎯 SUMMARY OF OPERATIONS ON LISTS")
print("- Concatenation (+): ✅")
print("- Merging (extend): ✅")
print("- Conversion: ✅")
print("- Aliasing: ✅")
print("- Cloning: ✅")
print("- Searching (in): ✅")
print("- Identity (is): ✅")
print("- Comparison (<,>): ✅")
print("- Emptiness (not): ✅")
print("="*70)
