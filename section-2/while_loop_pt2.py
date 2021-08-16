my_list = ["Apples", "Bananas", "Pineapples"]

for i in my_list:
    respons = input(f"Do you need some {i}? [y/N]> ")
    pass
# its like a placeholder in loop
    if respons.lower() == "y":
        print('Here you go')
        break
    
    continue
    

