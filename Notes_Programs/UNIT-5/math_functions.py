'''
math

Purpose:
Used for mathematical functions and constants.

Important Functions:

| Function            | Description             | Example                      |
| ------------------- | ----------------------- | ---------------------------- |
| `math.sqrt(x)`      | Square root             | `math.sqrt(25)`              |
| `math.pow(x,y)`     | x^y                     | `math.pow(2,5)`              |
| `math.floor(x)`     | Largest int ≤ x         | `math.floor(3.8)`            |
| `math.ceil(x)`      | Smallest int ≥ x        | `math.ceil(3.2)`             |
| `math.factorial(n)` | Factorial of n          | `math.factorial(5)`          |
| `math.gcd(a,b)`     | Greatest common divisor | `math.gcd(48,18)`            |
| `math.sin(x)`       | Sine (x in radians)     | `math.sin(math.radians(90))` |
| `math.cos(x)`       | Cosine (x in radians)   | `math.cos(0)`                |
| `math.log(x)`       | Natural log             | `math.log(10)`               |
| `math.log10(x)`     | Base-10 log             | `math.log10(100)`            |
| Constants           | `math.pi`, `math.e`     | `math.pi`, `math.e`          |


'''
# -------------------------------------------------------------
# Program: Important math module functions + OUTPUT
# -------------------------------------------------------------
import math

# sqrt()
print("Square root of 25:", math.sqrt(25))

# pow()
print("2^5 =", math.pow(2, 5))

# floor() and ceil()
print("\nFloor of 3.8:", math.floor(3.8))
print("Ceil of 3.2:", math.ceil(3.2))

# factorial()
print("\nFactorial of 5:", math.factorial(5))

# gcd()
print("\nGCD of (48, 18):", math.gcd(48, 18))

# trigonometric functions
print("\nsin(90°):", math.sin(math.radians(90)))
print("cos(0°):", math.cos(math.radians(0)))

# constants
print("\nValue of pi:", math.pi)
print("Value of e:", math.e)

# log()
print("\nNatural log of 10:", math.log(10))
print("Log base 10 of 100:", math.log10(100))


# -------------------------------------------------------------
# SAMPLE OUTPUT
# -------------------------------------------------------------
"""
Square root of 25: 5.0
2^5 = 32.0

Floor of 3.8: 3
Ceil of 3.2: 4

Factorial of 5: 120

GCD of (48, 18): 6

sin(90°): 1.0
cos(0°): 1.0

Value of pi: 3.141592653589793
Value of e: 2.718281828459045

Natural log of 10: 2.302585092994046
Log base 10 of 100: 2.0
"""
