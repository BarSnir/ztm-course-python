# decorators adding extra func to function as HOC (Higher order functions)

def my_decorator(func):
    def warp_func():
        print("*******")
        func()
        print("******* \n")
    return warp_func

@my_decorator
def print_hello():
    print("hello")

@my_decorator
def print_something_else():
    print("something else")

print_hello()
print_something_else()

