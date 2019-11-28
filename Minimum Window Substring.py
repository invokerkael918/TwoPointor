class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        # write your code here
        if not source:
            return ""
        if not target:
            return source
        allChars = source + target
        charSet = set(allChars)

        tMap = {}
        sMap = {}
        for key in charSet:
            sMap[key] = 0
            tMap[key] = 0
        for char in target:
            tMap[char] += 1

        right = 0
        n = len(source)
        count = len(set(target))  # count how many chars do we need to collect
        collected = 0  # how many chars we already counted
        ansl = -1
        ansr = -1
        for left in range(n):

            while (right < n and collected < count):
                sMap[source[right]] += 1

                if (sMap[source[right]] == tMap[source[right]]):  # reaching threshold
                    collected += 1
                right += 1
            if (collected == count):
                if (ansl == -1 or right - left < ansr - ansl):
                    ansl = left
                    ansr = right
            # source[left] is now removed from the window
            sMap[source[left]] -= 1
            if sMap[source[left]] == tMap[source[left]] - 1:
                collected -= 1
        if ansl == -1:
            return ""

        return source[ansl:ansr]

if __name__ == '__main__':
    S = Solution().minWindow("adfqeradboaf23098724huhfda923hadf78adfhadfhadfaodiyfas8","dfje89affefy8f")
    print(S)