my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0

for item in my_list:
    counter += item
    print(item, counter)

print('Az összeg: {}'.format(counter))
