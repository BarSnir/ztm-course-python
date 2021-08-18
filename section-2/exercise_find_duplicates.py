some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

for item in some_list:
    count = some_list.count(item)
    if count > 1:
        print(f"The item {item}, is duplicated {count} times.")
