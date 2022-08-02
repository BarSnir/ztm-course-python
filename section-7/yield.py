
def function_generator(num):
    for i in range(num):
        yield i*2

g = function_generator(10)
next(g)
next(g)
# handling one function in memory give us the power to pause the function
print(next(g))
# running the function in another instance
for item in function_generator(10):
    print(item)

