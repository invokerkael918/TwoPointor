class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        # write your code here
        left = 0
        ans = -0x7fffffff
        total = 0
        result = [-1, -1]
        for right in range(len(A)):

            if total < 0:
                total = A[right]
                left = right
            else:
                total += A[right]
            if total > ans:
                ans = total
                result[0] = left
                result[1] = right
        return result
if __name__ == '__main__':
    S = Solution().continuousSubarraySum([-3, -2, -5])
    print(S)