"""Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        temp = head
        while temp.next is not None:
            if temp.next.next is not None:
                next_node = temp.next.next
                temp.next.next = head
                head = temp.next
                temp.next = next_node
            elif temp.next.next is None:
                next_node = None
                temp.next.next = head
                head = temp.next
                temp.next = next_node
                break
        return head

# The solution's runtime beats 96.68% of python3 submissions(28ms)