class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        # write your code here
        n = len(nums)
        result = n + 1
        if len(nums) == 0 or sum(nums) < s:
            return -1

        right = 0
        total = 0
        for left in range(n):

            while right < n and total < s:
                total += nums[right]
                right += 1
            if total >= s:
                result = min(result, right - left)
            total -= nums[left]

        return result
