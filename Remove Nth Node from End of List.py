"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        temp = head
        node_index = length - n
        curr_i = 0

        if node_index == 0:
            head = temp.next
        else:
            while True:
                if curr_i == node_index - 1:
                    next_node = temp.next.next
                    temp.next = next_node
                    break
                temp = temp.next
                curr_i += 1

        return head
    #THIS BEATS 98% OF THE PYTHON3 SUBMISSIONS IN TERMS OF RUNTIME HECK YEAHHHHHHHHHHHHHHHHHHHHHHHH
    #It's super consuming of memory though lmao


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        main = dummy
        fast = dummy

        if main.next.next is None:
            head = None
            return head

        i = 0
        while i < n:
            fast = fast.next
            i += 1
            print(fast.val)

        while fast.next is not None:
            fast = fast.next
            main = main.next
        else:
            main.next = main.next.next

        return dummy.next