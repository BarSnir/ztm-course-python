my_set = {1, 2, 3, 4, 5, 6 , "a", "b", "c"}
my_set_new = {7, 2, 3, 9, 5, 6 , "a", "z", "c"}

# Diff
print(my_set.difference(my_set_new))

# Discard
my_set.discard(5)
print(my_set)

# Intersection
print(my_set.intersection(my_set_new))

# Diff updates
my_set.difference_update(my_set_new)
print(my_set)

# isDisJointed
print(my_set.isdisjoint(my_set_new))

# Union
# print(my_set.union(my_set_new))
print(my_set | my_set_new) # Shorthand of union

my_set = {"a", "c"}
my_set_new = {7, 2, 3, 9, 5, 6 , "a", "z", "c"}
# isSubset
print(my_set.issubset(my_set_new))

# issuperset
print(my_set.issuperset(my_set_new))
