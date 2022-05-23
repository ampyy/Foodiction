def calc(list1):
    if len(list1) == 0:
        return 0
    c = 0
    for x in list1:
        c += x
    return c/len(list1)

