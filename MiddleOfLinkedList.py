"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    在起点建立两个指针，一个走得快一个走的慢，快的走两个，慢的走一个，在快的不是None以及快的下一个不是None的情况，slow指向mid
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
        slow = head
        fast = slow.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow