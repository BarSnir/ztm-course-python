# := exists from py 3.8
a = [1, 2, 3, 4]
if (n := len(a)) < 10:
    print(f"Too short, current length is {n}")

while (n := len(a)) > 1:
    print(n)
    print(a)
    a = a[:-1]