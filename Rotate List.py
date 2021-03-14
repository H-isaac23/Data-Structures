"""Given the head of a linked list, rotate the list to the right by k places.
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        length = 0
        main = head
        while main:
            main = main.next
            length += 1
        num = k % length

        for i in range(num):
            main = head
            while main.next.next:
                main = main.next
            main.next.next = head
            head = main.next
            main.next = None

        return head

# Submission Detail
# Runtime: 48ms, faster than 21.32% of python3 submissions
# Memory: 14.3mb, better than 63.29% of python3 submissions
