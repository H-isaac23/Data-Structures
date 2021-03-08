"""Given the head of a singly linked list, return true if it is a palindrome.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        length = 0
        temp = head

        while temp:
            temp = temp.next
            length += 1

        if length % 2 == 0:
            length = int(length / 2)
        else:
            length = int((length // 2) + 1)

        temp = head
        for i in range(length):
            temp = temp.next

        head2 = temp

        while head2.next:
            next_node = head2.next.next
            head2.next.next = temp
            temp = head2.next
            head2.next = next_node

        main = head

        while temp:
            if temp.val != main.val:
                return False
            temp = temp.next
            main = main.next

        return True
