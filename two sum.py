def twoSum(nums, target):
    # O(n) time complexity
    see = {}
    for n in range(len(nums)):
        if target - nums[n] not in see:
            see[nums[n]] = n
        else:
            print ([see[target - nums[n]], n])


    # # O(nlog(n)) time complexity
    # nums.sort()
    # see = []
    # x = 0
    # y = len(nums) - 1
    # print (nums)
    #
    # while x < y:
    #     if nums[x] + nums[y] == target:
    #         see.append(x)
    #         see.append(y)
    #         x = x + 1
    #     elif nums[x] + nums[y] < target:
    #         x = x + 1
    #     else:
    #         y = y +1

    return see




print(twoSum([4, 2, 0, 4], 8))