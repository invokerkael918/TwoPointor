class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        result = []
        if len(nums) == 0:
            return [self.helper(lower, upper)]
        pre_point = lower - 1
        for point in nums:
            if pre_point != point and pre_point + 1 != point:
                # 不重叠，不相邻
                result.append(self.helper(pre_point + 1, point - 1))
            pre_point = point

        if nums[-1] < upper:
            # 计算末尾区间
            result.append(self.helper(nums[-1] + 1, upper))
        return result

    def helper(self, left_point, right_point):
        if left_point == right_point:
            return str(left_point)
        else:
            return str(left_point) + "->" + str(right_point)