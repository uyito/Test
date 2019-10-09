def fibb_iterative(data):
    arr = [0,1]
    if data < 0:
        return ("Fibb cant be less that 0")
    if data == 0:
        return arr[data]
    if data == 1:
        return arr[data]

    for i in range (2, data):
        current = arr[i-1] + arr[i-2]
        arr.append(current)


    return current, arr

def fibb_recursive(data):
    arr = [0, 1]
    if data < 0:
        return ("Fibb cant be less that 0")
    if data == 1:
        return 0
    if data == 2:
        return 1

    else:
        return fibb_recursive(data-1) + fibb_recursive(data-2)


def fibb_mem(data):
    a = 0
    b = 1

    if data == 0:
        return a

    if data == 1:
        return b

    for i in range(2, data):
        c = a + b
        a = b
        b = c

    return c, c-a, a


print (fibb_iterative(9))
print (fibb_recursive(9))
print (fibb_mem(9))




