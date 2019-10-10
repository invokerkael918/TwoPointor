class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here

        left = 0
        right = len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            # 上边两个while 一旦出来，此时的start 和end就是不符合标准的，
            # 只需要在下面的if判断他们还是，left<=right，就可以对他们进行交换了

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1

        return left
