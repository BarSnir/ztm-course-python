user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print('Only keys @ user->', item)

for item in user.values():
    print('Only values @ user.values()->', item)

for item in user.keys():
    print('Only keys @ user.keys()->', item)

for  key, value  in user.items():
    print('Keys & values @ user.items()->', key, value)

# Exercise
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0

for item in my_list:
    counter += item

print("Exercise count is->", counter)