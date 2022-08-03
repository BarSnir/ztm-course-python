def fib_function(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

g = fib_function(10)
for item in g:
    print(item)

