

# --------------------------------------------
# Section: What are functions?
# --------------------------------------------
# A function is a block of code that performs a specific task. Functions
# help modularize code and provide reuse.

def fun():
    """A tiny example function. Prints two lines."""
    print('My opinions may have changed')
    print('But not the fact that I am right')

# Calling the function multiple times
fun()  # first call
fun()  # second call

# Functions can be redefined; latest definition is used.

def fun():
    print('New definition of fun()')

fun()


# --------------------------------------------
# Communication with functions: parameters and return
# --------------------------------------------

def cal_sum(x, y, z):
    """Return sum of three numbers."""
    return x + y + z

s1 = cal_sum(10, 20, 30)
print('\ncal_sum(10,20,30) ->', s1)

# return without expression returns None

def empty_return():
    return

print('empty_return() ->', empty_return())

# returning multiple values: actually returns a tuple

def cal_sum_prod(x, y, z):
    ss = x + y + z
    pp = x * y * z
    return ss, pp  # returned as tuple

s, p = cal_sum_prod(10, 20, 30)
print('sum, product ->', s, p)

# If a function reaches end without return, it returns None

def no_return():
    a = 1 + 1

print('no_return() ->', no_return())

# --------------------------------------------
# Types of arguments: positional, keyword, *args, **kwargs
# --------------------------------------------
'''
Types of Arguments
Arguments in a Python function can be of 4 types:
(a) Positional arguments
(b) Keyword arguments
(c) Variable-length positional arguments
(d) Variable-length keyword arguments
Positional and keyword arguments are often called 'required'
arguments, whereas, variable-length arguments are called 'optional'
arguments.
Positional arguments must be passed in correct positional order. For
example, if a function expects an int, float and string to be passed to
it, then while calling this function the arguments must be passed in
the same order.
While passing positional arguments, number of arguments passed
must match with number of arguments received.
'''
# Positional arguments: order matters

def example_positional(i, j, k):
    print('\nInside example_positional: i + j =', i + j)
    print('k.upper() ->', str(k).upper())

example_positional(10, 3.14, 'Rigmarole')
# example_positional('Rigmarole', 3.14, 10)  # would be an error for .upper()

# Keyword arguments: order doesn't matter

def print_it(i, a, s):
    print('\nprint_it ->', i, a, s)

print_it(a=3.14, i=10, s='Sicilian') 
print_it(s='Sicilian', a=3.14, i=10)

# Mix positional and keyword: positional must come before keyword
print_it(10, a=3.14, s='Ngp')

#print_it(a=3.14, 10, s='Ngp')   #SyntaxError: positional argument follows keyword argument
#print_it(10, a=3.14, str='Ngp') #TypeError: print_it() got an unexpected keyword argument 'str'


'''
Sometimes number of positional arguments to be passed to a function is not certain.
In such cases, variable-length positional arguments can be received using *args.
args is a tuple.

Sometimes number of keyword arguments to be passed to a function is not certain.
In such cases, variable-length keyword arguments can be received using **kwargs.
kwargs is a dictionary.

We can use any other names in place of args and kwargs.
We cannot use more than one args and more than one kwargs while defining a function.

If a function is to receive required as well as optional arguments then they must occur in following order:
- positional arguments (required)
- variable-length positional arguments (optional)
- keyword arguments (required)
- variable-length keyword arguments (optional)
'''
# Variable-length positional arguments: *args

def show_args(*args):
    print('\nshow_args called with', len(args), 'args ->', args)
    for var in args:
        print(var, end=' ')
    print()

show_args(10)
show_args(10, 3.14)
show_args(10, 3.14, 'Sicilian')

# Variable-length keyword arguments: **kwargs

def show_kwargs(**kwargs):
    print('\nshow_kwargs called with', len(kwargs), 'kwargs ->', kwargs)
    for k, v in kwargs.items():
        print(k, ':', v)

show_kwargs(a=10)
show_kwargs(a=10, b=3.14)
dct = {'Student': 'Ajay', 'Age': 23}
show_kwargs(**dct)


# Order of parameters when mixing: positional, *args, keywords, **kwargs

def mixed(i, j, *args, x, y, **kwargs):
    print('\nmixed -> i, j, args, x, y, kwargs')
    print(i, j, args, x, y, kwargs)

mixed(10, 20, x=30, y=40)
mixed(10, 20, 100, 200, x=30, y=40, a=5, b=6)
#mixed(10, 20, 100, 200) #TypeError: mixed() missing 2 required keyword-only arguments: 'x' and 'y'


# Default arguments
# Note that while defining a function default arguments must follow non-default arguments.
print("\nDefault arguments")
def fun_defaults(a, b=100, c=3.14):
    print("a=",a,"b=",b,"c=",c)
    #return a + b + c

print('fun_defaults(10) ->', fun_defaults(10))
print('fun_defaults(20,50) ->', fun_defaults(20, 50))
print("fun_defaults(30,60,6.28) ->", fun_defaults(30, 60, 6.28))
print("fun_defaults(1, c=3, b=5) ->", fun_defaults(1, c=3, b=5))

# --------------------------------------------
# Unpacking arguments
# --------------------------------------------
'''
Suppose a function is expecting positional arguments and the
arguments to be passed are in a list, tuple or set.
In such a case we need to unpack the list/tuple/set using * operator before passing it
to the function.
'''

def print_five(a, b, c, d, e):
    print('\nprint_five ->', a, b, c, d, e)

lst = [10, 20, 30, 40, 50]
tpl = ('A', 'B', 'C', 'D', 'E')
s = {1, 2, 3, 4, 5}

print_five(*lst)
print_five(*tpl)
# For sets, order is arbitrary
print_five(*list(s))

# Unpacking dicts: keys (without **) or values (with **)
'''
Suppose a function is expecting keyword arguments and the
arguments to be passed are in a dictionary. In such a case we need
to unpack the dictionary using ** operator before passing it to the
function.
'''

def print_name_marks(name='Sanjay', marks=75):
    print('\nprint_name_marks ->', name, marks)

d = {'name': 'Anil', 'marks': 50}
# print_name_marks(*d)     # would pass keys: name, marks (as positional strings)
print_name_marks(**d)     # unpack as keyword args


# --------------------------------------------
# Inner functions and encapsulation
# --------------------------------------------
# Nested functions (inner function can access outer scope variables)

def outer():
    print('Reached outer')
    def inner():
        print('Inner avatar')
    inner()  # inner called inside outer

outer()
# inner()  # would raise NameError if uncommented — can't call inner here

'''
Suppose we wish to develop a function myrandom( ) to generate
random numbers. While executing this function we wish to check
whether a number is a prime number or not. We can do so by
defining a function isprime( ). But we do not want want isprime( ) to
be callable from outside myrandom( ). In a way we wish to protect
it. In such a case we can define isprime( ) as an inner function.
'''
def myrandom():
    import random
    def isprime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    r = random.randint(1, 100)
    return r, isprime(r)  # isprime is not visible outside myrandom

print('\nmyrandom ->', myrandom())





# --------------------------------------------
# Exercises from the chapter implemented as functions
# (Problem 13.1 to 13.9)
# --------------------------------------------

# Problem 13.1: sum and product
'''
Problem 13.1
Write a program to receive three integers from keyboard and get their
sum and product calculated through a user-defined function
cal_sum_prod( ).
'''

def cal_sum_prod_fn(x, y, z):
    """Return sum and product of three integers."""
    ss = x + y + z
    pp = x * y * z
    return ss, pp

# demonstration
print('\nProblem 13.1 ->', cal_sum_prod_fn(10, 20, 30))

# Problem 13.2: pangram check

def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

print('\nProblem 13.2 ->', ispangram('The quick brown fox jumps over the lazy dog'))
print('Problem 13.2 ->', ispangram("Crazy Fredrick bought many very exquisite opal jewels"))

# Problem 13.3: hyphen separated sort

def convert_hyphen(s1):
    items = [s for s in s1.split('-')]
    items.sort()
    s2 = '-'.join(items)
    return s2

s = 'here-come-the-dots-followed-by-dashes'
print('\nProblem 13.3 ->', convert_hyphen(s))

# Problem 13.4: create list of tuples (x, x^2, x^3) for 1..n

def generate_list(n=10):
    lst = []
    for i in range(1, n + 1):
        lst.append((i, i ** 2, i ** 3))
    return lst

print('\nProblem 13.4 ->', generate_list(10))

# Problem 13.5: palindrome check ignoring spaces and case

def ispalindrome(s):
    t = s.lower()
    left = 0
    right = len(t) - 1

    while right >= left:
        if t[left] == ' ':  # skip spaces on left
            left += 1
            continue
        if t[right] == ' ':  # skip spaces on right
            right -= 1
            continue
        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True

print('\nProblem 13.5 ->', ispalindrome('Malayalam'))
print('Problem 13.5 ->', ispalindrome('Rats live on no evil star'))
print('Problem 13.5 ->', ispalindrome('Murder for a jar of red rum'))

# Problem 13.6: remove duplicate words and sort them alphanumerically

def convert_remove_duplicates(s):
    words = [word for word in s.split(' ')]
    return ' '.join(sorted(list(set(words))))

s1 = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy"
print('\nProblem 13.6 ->', convert_remove_duplicates(s1))

s2 = "Sakhi was a singer because her mother was a singer, and Sakhi's mother was a singer because her father was a singer"
print('Problem 13.6 ->', convert_remove_duplicates(s2))

# Problem 13.7: count alphabets and digits

def count_alphabets_digits(s):
    d = {'Digits': 0, 'Alphabets': 0}
    for ch in s:
        if ch.isalpha():
            d['Alphabets'] += 1
        elif ch.isdigit():
            d['Digits'] += 1
        else:
            pass
    return d

print('\nProblem 13.7 ->', count_alphabets_digits('James Bond 007'))
print('Problem 13.7 ->', count_alphabets_digits('Kholi Number 420'))

# Problem 13.8: frequency of words in sorted order

def frequency(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = ('It is true for all that that that that '
            'that that that refers to is not the same that '
            'that that that refers to')
d = frequency(sentence)
print('\nProblem 13.8 -> Frequencies (sorted by word):')
for w in sorted(d):
    print(f"{w}:{d[w]}")

# Problem 13.9: create_sent1 and create_sent2

def create_sent1(sub, ver, obj):
    lst = []
    for i in range(len(sub)):
        for j in range(len(ver)):
            for k in range(len(obj)):
                sent = sub[i] + ' ' + ver[j] + ' ' + obj[k]
                lst.append(sent)
    return lst


def create_sent2(sub, ver, obj):
    return [s + ' ' + v + ' ' + o for s in sub for v in ver for o in obj]

subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV Serials', 'Netflix']

print('\nProblem 13.9 -> create_sent1:')
for l in create_sent1(subjects, verbs, objects):
    print(l)
print('\nProblem 13.9 -> create_sent2:')
for l in create_sent2(subjects, verbs, objects):
    print(l)

# --------------------------------------------
# Exercise set [A] examples (a) to (g)
# --------------------------------------------

# (a) count_lower_upper

def count_lower_upper(s):
    d = {'Lowercase': 0, 'Uppercase': 0}
    for ch in s:
        if ch.islower():
            d['Lowercase'] += 1
        elif ch.isupper():
            d['Uppercase'] += 1
    return d

print('\n[A-a] ->', count_lower_upper('Hello World ABC xyz'))

# (b) compute n + nn + nnn + nnnn (n as a digit/string)

def compute_n(n):
    # Accept n as digit or its string representation
    s = str(n)
    total = int(s) + int(s * 2) + int(s * 3) + int(s * 4)
    return total

print('\n[A-b] compute_n(4) ->', compute_n(4))
print('[A-b] compute_n(7) ->', compute_n(7))

# (c) create 3D array initialized to value

def create_array(x, y, z, value=None):
    # Return a 3D nested list with dimensions x, y, z each initialized to value
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

arr3d = create_array(2, 3, 4, value=0)
print('\n[A-c] create_array(2,3,4,0) -> dimensions and sample:', len(arr3d), len(arr3d[0]), len(arr3d[0][0]))

# (d) intersection of two lists

def create_list_intersection(a, b):
    # preserve order from first list, but remove duplicates in result
    seen = set()
    res = []
    for item in a:
        if item in b and item not in seen:
            res.append(item)
            seen.add(item)
    return res

print('\n[A-d] ->', create_list_intersection([1,2,3,4,2], [2,4,6]))

# (e) sanitize_list: remove duplicates

def sanitize_list(lst):
    # simple approach preserving order
    seen = set()
    res = []
    for item in lst:
        if item not in seen:
            res.append(item)
            seen.add(item)
    return res

print('\n[A-e] ->', sanitize_list([1,2,2,3,4,1,5]))

# (f) Which calls error? We'll implement the print_it from the question and show
# correct and incorrect calls as comments.

def print_it_question(i, a, s, *args):
    print()  # blank line
    print(i, a, s, end=' ')
    for var in args:
        print(var, end=' ')
    print()

# Valid calls:
print_it_question(40, 2.35, 'Nag', 'Mum', 10)
print_it_question(a=6.28, s='Hello', i=30)  # valid using keywords
print_it_question(20, s='Hi', a=6.28)  # valid
# print_it_question(10, 3.14)  # ERROR: missing required 's' argument

# (g) fun(a, *args, s='!') calls

def fun_question(a, *args, s='!'):
    print(a, s)
    for i in args:
        print(i, s)

fun_question(10)
fun_question(10, 20)
fun_question(10, 20, 30)
fun_question(10, 20, 30, 40, s='+')

# --------------------------------------------
# Exercise set [B] short answers implemented
# --------------------------------------------

# (a) What is passed to fun(a, lst) where a is int and lst is list?
# Answer: Two arguments: an integer and a list; both are passed by object reference.

# (b) Valid return statements:
# return (a, b, c)  # valid
# return a + b + c  # valid
# return a, b, c    # valid (returns tuple)

# (c) Demonstrate redefined function behaviour

def fun_redefined():
    print('First avatar')

# redefine

def fun_redefined():
    print('New avatar')

fun_redefined()

# (d) A function with three return statements returning different types

def multi_return(cond=0):
    if cond == 0:
        return 10  # int
    if cond == 1:
        return 'ten'  # str
    return [10]  # list

print('\n[B-d] ->', multi_return(0), multi_return(1), multi_return(2))

# (e) Can functions be nested? Yes — for scoping, helper functions, or hiding implementation.

# (f) How to call print_it to print elements of tpl?
# Use argument unpacking: print_it(*tpl)

# --------------------------------------------
# End of converted content
# --------------------------------------------

if __name__ == '__main__':
    print('\n--- End of LUP Chapter 13 demo file ---')
