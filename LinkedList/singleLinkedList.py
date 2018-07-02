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
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self,data):
        if self.head.data is None:
            self.head.data = data
        else:
            newNode = Node(data)
            ptrNode = self.head
            while ptrNode.next is not None:
                ptrNode = ptrNode.next
            ptrNode.next = newNode

    def __str__(self):
        ptrNode = self.head
        tmp = []
        while ptrNode is not None:
            tmp.append(ptrNode.data)
            ptrNode = ptrNode.next
        return str(tmp)

print("Linked List")
l = LinkedList()
ch = 0
while ch != 4:
    ch = int(input("\n1. Insert at Begining\n2. Insert at End\n3. Print the linked list\n4. Exit\nEnter your choice: "))
    if ch == 1:
        l.insertBeg(int(input("Enter data: ")))
    elif ch == 2:
        l.insertEnd(int(input("Enter data: ")))
    elif ch == 3:
        print(l)
