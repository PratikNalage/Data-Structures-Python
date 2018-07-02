class Node():
    '''A container for nodes'''

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    '''ADT for LinkedList'''

    def __init__(self,data=None):
        self.head = Node(data)

    def insertBeg(self,data):
        if self.head.data is None:
            self.head.data = data
            self.head.next = self.head
        else:
            newNode = Node(data)
            ptrNode = self.head
            while ptrNode.next != self.head:
                ptrNode = ptrNode.next
            ptrNode.next = newNode
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self,data):
        if self.head.data is None:
            self.head.data = data
            self.head.next = self.head
        else:
            newNode = Node(data)
            ptrNode = self.head
            while ptrNode.next != self.head:
                ptrNode = ptrNode.next
            ptrNode.next = newNode
            newNode.next = self.head

    def delete(self,data):
        if self.head.data is None:
            print("LinkedList is already empty")
        elif self.head.data == data:
            tempNode = self.head
            ptrNode = self.head
            while ptrNode.next != self.head:
                ptrNode = ptrNode.next
            self.head = self.head.next
            ptrNode.next = self.head
            del(tempNode)
        else:
            ptrNode = self.head.next
            preptrNode = ptrNode
            while ptrNode.data != data and ptrNode != self.head:
                preptrNode = ptrNode
                ptrNode = ptrNode.next
            preptrNode.next = ptrNode.next
            del(ptrNode)


    def __str__(self):
        ptrNode = self.head.next
        tmp = []
        tmp.append(self.head.data)
        while ptrNode != self.head:
            tmp.append(ptrNode.data)
            ptrNode = ptrNode.next
        return str(tmp)

print("Linked List")
l = LinkedList()
ch = [0]
while ch[0] != 5:
    ch = list(map(int,input("\n1. Insert at Begining(1,data)\n2. Insert at End(2,data)\n3. Print the linked list\n4. Delete a node(4,data)\n5. Exit\nEnter your choice: ").split()))
    if ch[0] == 1:
        l.insertBeg(ch[1])
    elif ch[0] == 2:
        l.insertEnd(ch[1])
    elif ch[0] == 3:
        print(l)
    elif ch[0] == 4:
        l.delete(ch[1])
