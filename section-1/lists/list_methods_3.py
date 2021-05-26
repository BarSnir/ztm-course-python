# Sort no.1
basket = ["a", "x", "b", "e", "f", "q", "g"]
basket.sort()
print("No1. Modified after print by list.sort():\n", basket, "\n")

# Sort no.2
basket = ["a", "x", "b", "e", "f", "q", "g"]
print("No2. No modified after print sorted():\n", sorted(basket), "\n")

# Reverse
basket.sort()
basket.reverse()
print("No3. Modified by list.reverse():\n", basket, "\n")

print("No4. Modified reverse with step of -1 from beging to end.\n", basket[::-1], "\n")

# Range list
print("No5. Range list 1 - 100:\n", list(range(1, 100)), "\n")


# Join
text = ' '
new_text = text.join(["Bar", "Snir"])
print("No6. Join method \n", new_text, "\n")