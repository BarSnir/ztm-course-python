username = input('Please enter your username:\n')
print(f'Welcome {username}')
password = input('Please enter your password:\n')
password_length = len(password)
hidden_password = "*" * password_length

print(f'{username}, your password {hidden_password} is {password_length} long.')