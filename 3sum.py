class Solution(object):
    def threeSum(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # print(nums)
        # nums = set(nums)
        # nums = list(nums)
        # print (nums)
        yes = []
        for x in range(0, len(nums)):
            sets = []
            for j in range(x+1, len(nums)):
                for i in range(j+1, len(nums)):
                    if nums[x] + nums[j] + nums[i] == 0:
                        sets.append(nums[x])
                        sets.append(nums[j])
                        sets.append(nums[i])
                        sets.sort()
                        yes.append(sets)
                        sets = []

        # print(yes)

        for x in range(len(yes)):
            # for j in range( x+1, len(yes)):
            #     if yes[x] == yes[j]:
            #         yes.remove(yes[j])
                    # print(yes)
            j = 1
            while j in range(x + 1, len(yes)):
            # if yes[x] in range (x+1, len(yes)) and yes[x] == yes[x+1]:
                if yes[x] == yes[j]:
                    # temp = yes[x]
                    yes.pop(j)
                    # yes.pop(x)
                    # yes.append(temp)
                    # print(temp)
                j = j + 1






        return yes

# li = [-1,0,1,2,-1,-4]
li = [0,0,0,0]

print(Solution().threeSum(li))
