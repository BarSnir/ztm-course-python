basket = [1, 2, 3, 4, 5]
# Length
print('length', len(basket))

# Append
basket.append(100)
new_list = basket.append(100)
print('Append', basket)
print('Returns', new_list)

# Insert
basket.insert(4, 6)
new_list = basket.insert(4, 6)
print('Inset', basket)
print('Returns', new_list)

# Extend at the End of list
basket.extend([7])
print('Extend', basket)

# Removing item
basket.pop()
print('Pop', basket)
basket.pop(0)
print('Pop with index', basket)

# Remove method
basket.remove(2)
print("Remove by value", basket)

# Pop received
index = 2
remove_item = basket.pop(index)
print(f"Remove item value from index {index}:", remove_item)

# Clear method
basket.clear()
print(f"Remove all items", basket)