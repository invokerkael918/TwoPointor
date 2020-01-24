class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
        一根指针扫描两个string. 当发现不相等的时候，我们就分三种情况。
    1。 去掉当前char。看剩余的子串是否相等。
    2。 去掉s的当前char，看剩余的两个子串是否相等。
    3。 去掉t的当前char, 看剩余的两个子串是否相等，

    有可能会出现，t就是s的子串的情况，这时候我们就要比较两者的长度差是否为1.
    比如： 'Frank' 和 'Fra'
    """

    def isOneEditDistance(self, A, B):
        # write your code here
        n = min(len(A), len(B))
        for i in range(n):
            if A[i] != B[i]:
                if len(A) == len(B):
                    return A[i + 1:] == B[i + 1:]

                return A[i + 1:] == B[i:] or A[i:] == B[i + 1:]

        diff = abs(len(A) - len(B))
        return diff == 1