from linkedlistpractice import Linkedlist

def partitioning (ll, value):
    curerntnode = ll.head
    ll.tail = ll.head
    # curerntnode.next = None

    while curerntnode:
        nextnode = curerntnode.next
        curerntnode.next = None 
        if curerntnode.value < value:
            curerntnode.next = ll.head
            ll.head = curerntnode
        else:
            ll.tail.next = curerntnode
            ll.tail = curerntnode
        curerntnode = nextnode

    if ll.tail.next is not None:
        ll.tail.next = None
            