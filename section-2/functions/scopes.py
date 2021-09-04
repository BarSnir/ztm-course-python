if True:
    x = 10


def some_func():
    total = 100

print(f"Printing x is in scope, total is not. value of x: {x}")

a = 1

def confusion():
    a = 20
    return a

print(f"Value of a is {a}, and not 20")
print(f"And value of a in confusion function is {confusion()}")

# Steps:
# 1. Going to local scope.
# 2. Parent local scope.
# 3. Global scope checking.
# 4. Built in Python functions.

scoped_variable = 2

def print_scoped_variable():
    def print_scoped_variable_execution():
        print(scoped_variable)
    return print_scoped_variable_execution()

print_scoped_variable()

# Using global variables

total = 0
# Bad way, be better with dependency injection.
def count():
    global total
    total += 1
    return total

print(count())
print(count())
print(count())


total_2 = 0
# Decencies injection.
def count(total_2):
    total_2 += 1
    return total_2

print(f"From dependencies injection {count(count(count(total_2)))}")

# Scope - what variables do I have access to?
# Similar to Cloujers
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions