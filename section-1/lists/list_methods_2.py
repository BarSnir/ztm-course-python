basket = [1, 2, 3, 4, 5]

# Index - find item (value, start, stop)
item = basket.index(2, 0, 4)

print("Index find:", item)
print( 2 in basket)
print( 7 in basket)
print("hey" in "hey there!")

# Count - count number of item appear
count = basket.count(5)
print("Number of times:", count)
