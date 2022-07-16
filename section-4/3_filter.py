def filter_nones(li):
    return li is not None and li % 2 == 0

my_list = [1 ,2 , 3, None, 0 ,18]
print(list(filter(filter_nones, my_list)))