# Enumerate structure
for index, char in enumerate('Kafka stack'):
    print("index & value->", index, char)


for index, char in enumerate(list(range(10))):
    if char == 5:
        print("The index of 5 is->", index)