class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        n = len(nums)
        result = []
        total = 0
        for i in range(n):
            total += nums[i]
            if i >= k - 1:
                result.append(total)
                total -= nums[i - k + 1]
        return result
