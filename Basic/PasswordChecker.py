print('hola')

username = input('You\'re user name: ')
password = input('You\'re password: ')

password_length = len(password)

secret_password = '*' * password_length

print(f'Hi {username} Your password {secret_password} is {password_length} character long.')
