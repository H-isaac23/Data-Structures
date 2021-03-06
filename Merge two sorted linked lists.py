"""Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            if l1 is None:
                return l2
            elif l2 is None:
                return l1

        dummy = ListNode()
        head = dummy

        if l1 and l2:
            t1 = l1.next
            t2 = l2.next
            while l1 and l2:
                if l1.val > l2.val:
                    dummy.next = l2
                    dummy = dummy.next
                    l2 = t2
                    if t2 is None:
                        break
                    t2 = t2.next
                else:
                    dummy.next = l1
                    dummy = dummy.next
                    l1 = t1
                    if t1 is None:
                        break
                    t1 = t1.next

            if l1 is None:
                dummy.next = l2
            elif l2 is None:
                dummy.next = l1

        return head.next

# Submission Details
# Runtime: 36ms, faster then 76.54% of python3 submissions
# Memory: 14mb, better then 96.50% of python3 submissions
