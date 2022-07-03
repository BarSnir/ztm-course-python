
class DecoratorsExample:

    def __init__(self, name, age):
        return

    @classmethod
    def sum(cls, num1, num2):
        return cls('Bar', num1 + num2)

    @staticmethod
    def sum2(num1, num2) -> int:
        return num1 + num2

print(DecoratorsExample.sum(1, 2))
print(DecoratorsExample.sum2(1, 2))