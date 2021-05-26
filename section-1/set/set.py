# set unordered collection of unique objects 
my_set = {1, 2, 3, 4, 5, 5}
# add
my_set.add(100)
print(my_set)

#convert list
my_list = [1, 2, 3, 3, 5 , 6, 6]
new_set = set(my_list)
print(new_set)

print(1 in new_set)
print(len(new_set))
print(list(new_set))