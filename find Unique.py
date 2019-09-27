def find_unique(data):
    for x in range(0, len(data)):
        duplicate = False
        for y in range(x + 1, len(data)):
            if data[x] == data[y]:
                duplicate = True
            break

    if duplicate is False:
        return data[x]