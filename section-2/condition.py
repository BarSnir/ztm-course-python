condition = True

if condition and not True:
    print('It will not print.')
elif condition is not False:
    print('It will print.') 
elif condition is not 0j:
    print('It will print.') 
else:
    print('It will not print.')


message = "Content" if condition is True else False
print(message)