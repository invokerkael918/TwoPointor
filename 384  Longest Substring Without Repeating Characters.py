class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        n = len(s)
        if n == 1:
            return 1
        result = 0
        right = 0
        dic = set([])
        for i in range(n):
            while right < n and s[right] not in dic:
                dic.add(s[right])
                right += 1
            result = max(result, right - i)
            dic.remove(s[i])
        return result
