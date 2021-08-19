def sum(a, b):
    return a + b

def main_function(a, b):
    def nested_function(n1, n2):
        return n1 + n2
    return nested_function(a, b)

calculation = main_function(10, 1)
print(calculation)

# docstrings

def test(a):
    '''
    Info: this is function print param a
    '''
    print(a)

test('a')
print(test.__doc__)
# help(test)