from linkedlistpractice import Linkedlist

def removedups (ll):
    if ll.head is None:
        return
    else:
        currentnode = ll.head
        visited = set([currentnode.value])
        while currentnode.next:
            if currentnode.next.value in visited:
                currentnode.next = currentnode.next.next
            else:
                visited.add(currentnode.next.value)
                currentnode = currentnode.next
        return ll


customlikedlist = Linkedlist()
customlikedlist.generate(10, 0, 99)
print (customlikedlist)
removedups(customlikedlist)
print (customlikedlist)
