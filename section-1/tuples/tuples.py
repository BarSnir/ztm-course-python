# Tuples - immutables list
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = "z"

print("Index in tuple:", my_tuple[2], "\n")
print("Boolean in tuple:", 2 in my_tuple, "\n")

# Because tuple are immutable, we can use them as keys in dict:", "
some_dict = {
    (1, 2): [1, 2, 3]
}

print("With tuple key of (1, 2):", some_dict[(1, 2)], "\n")

x, y, z, *other = my_tuple
print("x", x, "\n")
print("y", y, "\n")
print("z", z, "\n")
print("other", other, "\n")