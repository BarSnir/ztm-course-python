def get_highest_even(li):
    even_list = []
    for item in li:
        if item % 2 == 0:
            even_list.append(item)
    return max(even_list)

result = get_highest_even([1, 2, 3, 4, 5, 6, 7])
print(result)