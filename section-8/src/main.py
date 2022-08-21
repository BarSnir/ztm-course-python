import utility
from package import shopping_cart
# OR from package.shopping_cart import add_to_shopping_cart

print(utility)
print(utility.sum(1, 2))
cart = shopping_cart.add_to_shopping_cart({'price': 1})
print(cart)