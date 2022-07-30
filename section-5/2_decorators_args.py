# decorators adding extra func to function as HOC (Higher order functions)

def my_decorator(func):
    def warp_func(*args, **kwargs):
        print("*******")
        func(*args, **kwargs)
        print("******* \n")
    return warp_func

@my_decorator
def print_greeting(greeting):
    print(greeting)

# a = my_decorator(print_greeting)
print_greeting("Greetings from Bar.")