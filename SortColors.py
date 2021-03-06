class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] == 0:
                left += 1
            while left <= right and nums[right] != 0:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        start, end = left, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] == 1:
                start += 1
            while start <= end and nums[end] != 1:
                end -= 1

            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                left += 1
                right -= 1

        return nums
