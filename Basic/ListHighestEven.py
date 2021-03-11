def highesteven(li):
    sort_list = li
    sort_list.sort(reverse=True)
    # print(sort_list)

    for item in sort_list:
        if item % 2 == 0:
            return item
            break
        else:
            continue
    return item


print(highesteven([11, 2, 6, 9, 8, 10, 15]))
