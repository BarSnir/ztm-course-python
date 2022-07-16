from functools import reduce

my_list = [1, 2, 3, 4, 5]


def accumulator(acc, x):
    return acc + x
    
# default value to 0
print(reduce(accumulator, my_list, 0))