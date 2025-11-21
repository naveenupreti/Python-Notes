# Indirect Recursion Example:
# is_even() calls is_odd(), and is_odd() calls is_even()

def is_even(n):
    """
    Function to check if a number is even.
    Uses indirect recursion by calling is_odd().
    """

    if n == 0:
        # Base case: 0 is even
        return True
    
    # Recursive case: reduce n by 1 and check if (n-1) is odd
    return is_odd(n - 1)


def is_odd(n):
    """
    Function to check if a number is odd.
    Uses indirect recursion by calling is_even().
    """

    if n == 0:
        # Base case: 0 is NOT odd
        return False
    
    # Recursive case: reduce n by 1 and check if (n-1) is even
    return is_even(n - 1)


# Test the functions
num1 = 10
num2 = 7

print("Is", num1, "even?", is_even(num1))
print("Is", num2, "odd?", is_odd(num2))


'''
Memory Stack Diagram

is_even(4)
┌────────────────────────────┐
│ is_even(0)                 │
│  n = 0                     │
│  returns True              │
├────────────────────────────┤
│ is_odd(1)                  │
├────────────────────────────┤
│ is_even(2)                 │
├────────────────────────────┤
│ is_odd(3)                  │
├────────────────────────────┤
│ is_even(4)                 │
└────────────────────────────┘


is_odd(5)
┌─────────────────────────────┐
│ is_even(0)                  │
│ n = 0                       │
│ returns True                │
├─────────────────────────────┤
│ is_odd(1)                   │
├─────────────────────────────┤
│ is_even(2)                  │
├─────────────────────────────┤
│ is_odd(3)                   │
├─────────────────────────────┤
│ is_even(4)                  │
├─────────────────────────────┤
│ is_odd(5)                   │
└─────────────────────────────┘


is_odd(4)

┌────────────────────────────┐
│ is_odd(0)                  │
│  n = 0                     │
│  returns False             │
├────────────────────────────┤
│ is_even(1)                 │
├────────────────────────────┤
│ is_odd(2)                  │
├────────────────────────────┤
│ is_even(3)                 │
├────────────────────────────┤
│ is_odd(4)                  │
└────────────────────────────┘

is_even(5)

┌────────────────────────────┐
│ is_odd(0)                  │
│  n = 0                     │
│  returns False             │
├────────────────────────────┤
│ is_even(1)                 │
├────────────────────────────┤
│ is_odd(2)                  │
├────────────────────────────┤
│ is_even(3)                 │
├────────────────────────────┤
│ is_odd(4)                  │
├────────────────────────────┤
│ is_even(5)                 │
└────────────────────────────┘

'''
