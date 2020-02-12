class Solution:
    """
    @param num: A list of integers
    @return: An integer
    拿那个[100, 4, 200, 1, 3, 2]样例，你该怎么数数呢？你先从100数，然后呢，就没有了。再从4开始数，唉，不对，不应该，因为后面还有3，2，1
    所以应该把4跳过去，待会从小的数开始数。再后面是200，因为没有199，所以应该从200开始。
    """
    def longestConsecutive(self, num):
        # write your code here
