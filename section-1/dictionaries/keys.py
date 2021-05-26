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
user = dict(name="Bar")
print("Creating dict from dict():", user, "\n")
