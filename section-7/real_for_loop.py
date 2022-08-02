print("\n================================")
print("For loops under the hood")
print("\n================================")
def for_loop_under_the_hood(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

for_loop_under_the_hood([1, 2, 3])
print("\n================================")
print("Generator under the hood")
print("\n================================")
class MyGenerator:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration


gen = MyGenerator(0 , 100)

for i in gen:
    print(i)