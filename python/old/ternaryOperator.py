# ternaryOperator.py
# A "tenary operator" is a shortcut for conditional expression to assign
# one or another value if the condition is true or false.
# It was added to Python 2.5, check it:
# https://mail.python.org/pipermail/python-dev/2005-September/056846.html

# The syntax for a ternary operator is:
# x = A if C else B

# Literally, it coul be:
# x will be A if C is given, otherwise x will be B

# More examples:
# x will be "Bigger" if a is bigger than b, otherwise will be "Lower"
a, b = 7, 10
x = "Bigger" if a > b else "Lower"
print(x)

# This is a way to simplify in one line the next block:
if a > b:
    x = "Bigger"
    print(x)
else:
    x = "Lower"
    print(x)

# Using a lambda function
# This will retrieve a warning beucase:
# "do not assign a lambda expression, use a def E731
x = lambda: "Bigger" if a > b else "Lower"

x()


# Using an one-liner function
def x(a, b): return "Bigger" if a > b else "Lower"


# This is a way to avoid the next:
def xFunc(a, b):
    if a > b:
        x = "Bigger"
        print(x)
    else:
        x = "Lower"
        print(x)


xFunc(a, b)
