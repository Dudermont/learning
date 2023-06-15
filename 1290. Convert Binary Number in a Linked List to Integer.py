# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        list1 = []

        while head:
            list1.append(head.val)
            head = head.next

        lengh = len(list1)
        dec = 0

        for i in range(0, lengh):
            dec += list1[i] * (2 ** (lengh - i - 1))
        return dec
