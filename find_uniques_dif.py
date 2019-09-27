def contains(list, element):
    for x in list:
        if x == element:
            return True
    return False


# return true if element is in list

def diff(listA, listB):
    num_not_in = []
    not_in = []
    lst = 0
    num_of_list = len(listA)
    while lst < num_of_list:
        if contains(listB, listA[lst]) == False:
            lst = 1 + lst
        else:
            not_in.append(listA[lst])
    num_not_in.append(not_in)
    lst = 0
    not_in = []
    num_of_list = len(listB)
    while lst < num_of_list:
        if contains(listA, listB[lst]) == False:
            lst = 1 + lst
        else:
            not_in.append(listB[lst])
    num_not_in.append(not_in)

    return num_not_in

x = [1, 2, 3, 4]
y = [1, 2, 3, 5]

print(diff(x, y))
#
# for list in listA:
#
#
# if list not in listB:
#     not.append[list]
