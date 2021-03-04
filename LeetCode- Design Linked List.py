class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None:
            return -1

        temp = self.head
        for i in range(index + 1):
            if i == index:
                break
            elif temp.next is not None:
                temp = temp.next
            else:
                return -1

        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        temp = self.head
        if self.head is None and index == 0:
            self.head = Node(val)
        elif index == 0:
            new_node = Node(val)
            new_node.next = temp
            self.head = new_node
        elif self.head is None and index > 0:
            pass
        else:
            for i in range(index + 1):
                if i == index - 1 and temp is not None:
                    next_node = temp.next
                    temp.next = Node(val)
                    temp.next.next = next_node
                elif temp is None:
                    break
                else:
                    temp = temp.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        temp = self.head
        if index == 0:
            self.head = temp.next
        else:
            for i in range(index + 1):
                if i == index - 1 and temp.next is not None:
                    temp.next = temp.next.next
                elif temp is None:
                    break
                else:
                    temp = temp.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)