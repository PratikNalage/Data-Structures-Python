class Node():
    '''A container for nodes'''

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    '''ADT for LinkedList'''

    def __init__(self,data=None):
        self.head = Node(data)
        self.tail = self.head

    def insertBeg(self,data):
        if self.head.data is None:
            self.head.data = data
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertEnd(self,data):
        if self.head.data is None:
            self.head.data = data
        else:
            newNode = Node(data)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def delete(self,data):
        if self.head.data is None:
            print("LinkedList is already empty")
        elif self.head.data == data:
            tempNode = self.head
            if self.head == self.tail:
                self.head.data = self.tail.data = None
            else:
                self.head = self.head.next
                self.head.prev = None
            del(tempNode)
        else:
            ptrNode = self.head.next
            preptrNode = self.head
            while ptrNode.data != data:
                preptrNode = ptrNode
                ptrNode = ptrNode.next
            if ptrNode == self.tail:
                self.tail = preptrNode
                preptrNode.next = None
            else:
                preptrNode.next = ptrNode.next
                ptrNode.next.prev = preptrNode
            del(ptrNode)


    def __str__(self):
        ptrNode = self.tail
        tmp = []
        while ptrNode is not None:
            tmp.append(ptrNode.data)
            ptrNode = ptrNode.prev
        return str(tmp)

print("Linked List")
l = LinkedList()
ch = 0
while ch != 5:
    ch = int(input("\n1. Insert at Begining\n2. Insert at End\n3. Print the linked list(Reversed)\n4. Delete a node\n5. Exit\nEnter your choice: "))
    if ch == 1:
        l.insertBeg(int(input("Enter data: ")))
    elif ch == 2:
        l.insertEnd(int(input("Enter data: ")))
    elif ch == 3:
        print(l)
    elif ch == 4:
        l.delete(int(input("Enter data: ")))
