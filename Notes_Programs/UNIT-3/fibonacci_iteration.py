#finds the nth fibonacci number using iteration
def fib_itr(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_itr(6))
