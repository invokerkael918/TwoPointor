class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        ans = float('inf')
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right] + numbers[i]
                if target == sum:
                    return sum
                if abs(sum - target) < abs(ans - target):
                    ans = sum

                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return ans