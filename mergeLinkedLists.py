class Node:
    data = None 
    next = None 

    def __init__(self,data, next) -> None:
        self.data = data 
        self.next = next

class LinkedList:
    head = None 
    def __init__(self) -> None:
        self.head = None
    
    def printList(self):
        temp = self.head
         
        while temp :
            print(temp.data, end="->")
            temp = temp.next



def merge(linkedList1:Node, linkedList2:Node):
    aux = Node(0,None) 
    tail = aux

    while 1:

        if linkedList1 is None:
            tail.next = linkedList2
            break

        if linkedList2 is None:
            tail.next = linkedList1
            break

        if linkedList1.data <= linkedList2.data:
            tail.next = linkedList1
            linkedList1 = linkedList1.next
        
        else:
            tail.next = linkedList2
            linkedList2 = linkedList2.next
    
        tail = tail.next

    return aux.next

def main():
    ll = LinkedList()

    ll.head = (merge(Node(1,Node(2,Node(3,None))), Node(4,Node(5,Node(6,None)))))
    ll.printList()
    print()
    ll.head = (merge(Node(1,Node(3,Node(5,None))), Node(2,Node(4,Node(6,None)))))
    ll.printList()
    print()
    ll.head = (merge(Node(4,Node(4,Node(7,None))), Node(1,Node(5,Node(6,None)))))
    ll.printList()
    print() 


if __name__ == "__main__":
    main()