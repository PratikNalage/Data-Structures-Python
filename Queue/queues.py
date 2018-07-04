class Queue():
    '''An ADT for Queue'''
    def __init__(self):
        self.qu = []

    def enqueue(self,data):
        self.qu.append(data)

    def dequeue(self):
        if self.qu == []:
            return None
        return self.qu.pop(0)


if __name__ == '__main__':
    print("Queue")
    q = Queue()
    ch = [0]
    while ch[0] != 3:
        ch = list(map(int,input("\n1. enqueue(1 data)\n2. dequeue\n3. Exit\nEnter your choice: ").split()))
        if ch[0] == 1:
            q.enqueue(ch[1])
        elif ch[0] == 2:
            print(q.dequeue())
