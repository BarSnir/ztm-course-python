# *args **kwargs

def super_func(*args):
    print(f"args are {args}")
    return sum(args)

results = super_func(1, 2, 3, 4)
print(f"The result is {results}")

def super_func_2(**kwargs):
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return total

results = super_func_2(num1=6, num2=7)
print(f"The result is {results}")

# Rule: paramters, *args, default paramters, **kwargs
def test(param, *args, i="default", **kwargs):
    pass