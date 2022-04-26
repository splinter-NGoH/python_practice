

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None



class Slinked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert
    def insert_singllinkedlist (self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None 
                self.tail.next = new_node
                self.tail =new_node
            else:
                tempNode = self.head
                index = 0
                while index < location -1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = new_node
                new_node.next = nextNode

    # traverse throw limked list node
    def traverseSll (self):
        if self.head is None:
            print ('The singlylinkedlist doesn\'t exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    def linkedlistsearch (self, value):
        if self.head is None:
            print('linkedlistsearch exit no item ')
            exit()
        else:
            node = self.head
            while node is not None:
                if node.value == value:    
                    print(node.value)
                node = node.next
            return 'value doesn\'t exist'
    
    def deleteNode(self, location):
        if self.head is None:
            print('dosnt exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextnode = tempNode.next
                tempNode.next = nextnode.next
    def deletelinkedlist(self):
        if self.head is None:
            print (' no linked list')
        else:
            self.head = None
            self.tail = None





singlylinkedlist = Slinked_list()
singlylinkedlist.insert_singllinkedlist(1,1)
singlylinkedlist.insert_singllinkedlist(2,1)
singlylinkedlist.insert_singllinkedlist(3,1)
singlylinkedlist.insert_singllinkedlist(4,1)
singlylinkedlist.insert_singllinkedlist(0,0)
print([node.value for node in singlylinkedlist])
singlylinkedlist.deleteNode(1)
print([node.value for node in singlylinkedlist])

# singlylinkedlist.traverseSll()
singlylinkedlist.linkedlistsearch(4)