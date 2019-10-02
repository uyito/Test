def contains(list, element):
    for x in list:
        if x == element:
            return True
    return False


# return true if element is in list

def diff(list_a, list_b):
    num_not_in = []
    not_in = []
    lst = 0
    num_of_list = len(list_a)
    while lst < num_of_list:
        if contains(list_b, list_a[lst]) == False:
            lst = 1 + lst
        else:
            not_in.append(list_a[lst])
    num_not_in.append(not_in)
    lst = 0
    not_in = []
    num_of_list = len(list_b)
    while lst < num_of_list:
        if contains(list_a, list_b[lst]) == False:
            lst = 1 + lst
        else:
            not_in.append(list_b[lst])
    num_not_in.append(not_in)

    return num_not_in

x = [1, 2, 3, 4]
y = [1, 2, 3, 5]

print(contains(y, 4))
print(diff(x, y))

# for list in listA:
#
#
# if list not in listB:
#     not.append[list]
