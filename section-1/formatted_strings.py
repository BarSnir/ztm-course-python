# Formatted strings
name = input("You username please:")
# Python 2
msg = "Hello Mr {name}, good to see you.".format(name=name)
print(msg)
print("Hello Mr {}, good to see you.".format("Bar"))
print("Hello Mr {}, good to see you.".format(name))
print("Hello Mr {name}, good to see you.".format(name=name))
print("Hello Mr {1}, good to see you.{0}".format(name, "some text"))
# Python 3
print(f"Hello Mr {name}, good to see you.")