'''
Scope and LEGB Rule
 Scope of an identifier indicates where it is available for use.
 Scope can be Local (L), Enclosing (E), Global (G), Built-in (B).
 Scope becomes more and more liberal from Local to Built-in.
'''

# Global variable (G in LEGB)
x = 10

# Using global x here
print(len(str(x)))   # Converts x to string → "10" → length = 2


def fun1():  # fun1 creates an Enclosed scope (E in LEGB)
    y = 20   # Local to fun1 (L in LEGB)

    print(x, y)          # x → found in Global, y → found in fun1 local
    print(len(str(x)))   # x still comes from Global scope

    def fun2():  # fun2 creates a new inner function scope (new L)
        z = 30   # Local to fun2 (L in LEGB for fun2)

        # LEGB search order inside fun2:
        # L → y? no, z? yes (z = 30)
        # E → y = 20 (from fun1)  
        # G → x = 10  
        # B → built-ins
        print(x, y, z)       # x (Global), y (Enclosed), z (Local)
        print(len(str(x)))   # x again found from Global

    fun2()  # Call inner function

# Start execution
fun1()
'''
LEGB Resolution Breakdown
L — Local

    Inside fun2: z

    Inside fun1: y

E — Enclosed

    Inside fun2, the enclosing scope provides y

G — Global

    x is found in the global namespace

B — Built-ins

    len(), str() come from Python’s built-ins
'''