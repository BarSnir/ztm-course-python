my_set = {char for char in 'hello'}
print(my_set)

simple_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

my_dict = { k+'_new':v**2 for k, v in simple_dict.items() if v%2==0}
print(my_dict)