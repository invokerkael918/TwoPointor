class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # write your code here
        if len(heights) < 3:
            return 0

        left, right = 0 , len(heights) - 1
        maxLeft, maxRight = 0, 0
        total = 0
        while left < right:
            if heights[left] <= heights[right]:
                maxLeft = max(heights[left],maxLeft)
                total += maxLeft - heights[left]
                left+=1
            else:
                maxRight = max(heights[right],maxRight)
                total+= maxRight - heights[right]
                right-=1

        return total