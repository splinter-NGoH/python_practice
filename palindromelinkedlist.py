class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class IsPalindrome:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_palindrome(self, head: ListNode):
        node = head
        while node is not None:
            current_node = ListNode(node)
            self.linked_list.head = current_node

            current_node.next = self.linked_list.head
            node = node.next


paladin = IsPalindrome()
print(paladin.is_palindrome(head=[1, 2]))
