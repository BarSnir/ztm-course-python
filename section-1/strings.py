'this is a string'
"This is also a string"
print(type("This is also a string"))

username = "username"
password = "password"
long_String = """
This is also a string
"""

print(long_String)
firstname = "Bar"
lastname = "Schlinger"
full_name = firstname +" "+ lastname
print(full_name)

# String concatenation
print('hello' + ' ' +'Bar'+ ' '+ str(5))
# String conversion
print(type(str(5)))

# Escape sequences
weather = "It's sunny kind of \"sunny\""
weather_with_tab = "\t It's sunny kind of \"sunny\""
print(weather_with_tab)
weather_with_tab = "\b It's sunny kind of \"sunny\""
print(weather_with_tab)
weather_with_tab = "It's sunny kind of \n \"sunny\""
print(weather_with_tab)