# Program: Multiplication tables for a given range with proper formatting

# Take input for range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# Loop through each number in the range
for num in range(start, end + 1):
    #print(f"\nMultiplication Table of {num}") # python 3.6 and above
    print("\nMultiplication Table of {}".format(num))
    print("-" * 25)
    
# Multiplication from 1 to 10
for i in range(1, 11):
    # Align numbers nicely using format specifiers
    #print(f"{num:>3} x {i:>2} = {num*i:>4}") # python 3.6 and above
    print("{:>3} x {:>2} = {:>4}".format(num, i, num*i))
