my_list = ['a', 'b', 'c', 'd', 'c', 'n', 'd', 'q']

duplicates = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print("Dupla elemek listája: {duplicates}".format)
