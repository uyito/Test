# Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.
#
# 3 2 3 1 4 1 1 3   (million dollars)
#
# 7 (million dollars)
#
# Goal: longest possible segment within budget
#
# 1 -> 1 -> 2 ->
#
# Valid cases:
# 3
# 3 2
# 3 2 3
# 3 2 3 1
# 2 3 1
#
# Invalid segments:
# 3 (2) 3 1

def long_seg(blocks, cash):
    brick = []
    seg_of = []
    num_block = {}

    # cash_left = cash
    # new = 0
    for x in range (len(blocks)):
        count = 1
        sum_num = blocks[x]
        seg = list()
        seg.append(blocks[x])
        for y in range(x+1, len(blocks)):
            # sum = y + sum + new
            # sum = x+y+new
            # print(blocks[y])
            if cash - (sum_num + blocks[y]) >= 0:
                count = count + 1
                sum_num = sum_num +blocks[y]
                # print()
                seg.append(blocks[y])
                # new = x+y
            else:
                seg_of.append(seg)
                brick.append(count)
                num_block[count] = seg
                break

    print(seg_of)
    print(brick)
    x = max(num_block)
    print(x, "=" , num_block[x])
    print(num_block)


n = [3, 2, 3, 1, 4, 1, 1, 3]
ch = 7

long_seg(n, 7)
