class Node ():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Creationdoublylnkedlist ():
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def __iter__ (self): 
        node = self.head
        while node:
            yield node
            node = node.next
        
    def creatlistdoubly (self, value):
        node = Node(value) 
        self.tail = node
        self.head = node
        node.next = None
        node.prev = None
        return 'linked list is created successfully'

    def insertion(self, nodevalue, location):
        if self.head is None:
            print ('The node can\'t be inserter')
        else:
            newnode = Node(nodevalue)
            if location == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif location == -1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode = newnode
            

creatlist = Creationdoublylnkedlist()
creatlist.creatlistdoubly(4)
print ([node.value for node in creatlist])
creatlist.insertion(0,0)
creatlist.insertion(1,0)
creatlist.insertion(2,-1)
print ([node.value for node in creatlist])
