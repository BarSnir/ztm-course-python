# Range is a generator
range(100)

def make_list(num):
    return [i*2 for i in range(num)]

print(make_list(100))

