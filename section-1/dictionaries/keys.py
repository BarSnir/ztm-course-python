#keys

some_dict = {
    123: "Can be integer",
    True: "Can be also boolean",
    "only-immutables": "And of curse..strings",
    False: "Key must be unqiue"
}

print(
    some_dict[123],
    "\n",
    some_dict[True],
    "\n",
    some_dict["only-immutables"], 
    "\n",
    some_dict[False],
    "\n"
)

# Avoiding key error
print("Avoiding key error by .get(key):", some_dict.get("None-exists-key"), "\n")
print("Set default:", some_dict.get("None-exists-key", "exists"), "\n")


# Creating new dict
user = dict(name="Bar", price=1000)
print("Creating dict from dict():", user, "\n")

print("check key in dict:", "size" in user, "\n")
print("check value in dict:", "Bar" in user.values(), "\n")
print("get the items in dict:", user.items(), type(user.items()), "\n")


# Copying
user2 = user.copy()
print("Copying an dict:", user, "(user)", user2, "(user2)", "\n")

# Update
user2.update({"name": "john"})
print("After updating name key in user2:", user2, "\n")

# Pop key & value
user.pop("name")
print("user after poping name:", user, "\n")

# Clear dictionary
user.clear()
print("Cleaning: ", user, "\n")
