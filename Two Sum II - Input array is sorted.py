class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        h = {}
        # [2,7,10,15]
        # {2: 1}

        for i, num in enumerate(nums):

            if target - num not in h:
                h[num] = i

            else:
                return [h[target - num] + 1, i + 1]
