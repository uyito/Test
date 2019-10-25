temp = []
def deep_learn(arr):
    length_arr = len(arr)
    x = 0
    while x < length_arr:
        if type(arr[x]) == type(temp):
            deep_learn(arr[x])
        else:
            print(arr[x])
        x = x + 1

data = [2, [3, 4,[1, 2], 5], 6, 7]

deep_learn(data)

