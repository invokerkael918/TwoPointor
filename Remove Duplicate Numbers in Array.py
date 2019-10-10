class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        s, count_set = set(), 0

        # countSet用来记录加了多少个元素进入d
        # 在加入的同时count
        for num in nums:
            if num not in s:
                s.add(num)
                nums[count_set] = num
                count_set += 1

        return count_set
