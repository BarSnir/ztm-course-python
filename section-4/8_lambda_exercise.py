my_list = [1, 2, 3]

square_results = list(map(lambda x: x**2, my_list))
print(square_results)


a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
