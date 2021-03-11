# Small Funny GUI program

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# print(len(picture))

item = 0
while item < len(picture):
    my_pic = ''
    for i in picture[item]:
        if i == 0:
            my_pic += ' '
        elif i == 1:
            my_pic += '*'
    print('\n', my_pic)
    item += 1
