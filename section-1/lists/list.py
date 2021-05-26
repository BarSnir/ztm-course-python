list
li = [1, 2, 3, 4, 5]
li2 = [1, 'b', 'a', 2, bool]

# Section - 2, list slicing
amazon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes',
]
# Example for copying vs pointing
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
# In this print below, be aware, u creating instance of the list.
print(amazon_cart[0::2])
print(amazon_cart)