# String are iterable
for item in "This is my python course":
    print(item)

# Lists are iterable
for item in [1, 2, 3, 4]:
    print("Lists are iterable->", item)

# Sets are iterable
for item in {1, 2, 3, 4}:
    print("Sets are iterable->", item)

# Tuples are iterable
for item in (1, 2, 3, 4):
    print("Tuples are iterable->", item)

for item in [1, 2, 3, 4]:
    for x in ['a', 'b', 'c']:
        print(f"With item {item} we got nested value of {x}") 

print("The last value of item is->", item)