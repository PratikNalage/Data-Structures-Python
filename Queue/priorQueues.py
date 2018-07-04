class Queue():
    '''An ADT for Queue'''
    def __init__(self):
        self.qu = []

    def enqueue(self,data,prior):
        i=-1
        for d,p in self.qu:
            if prior < p:
                i = self.qu.index([d,p])
                break
        if i==-1:
            self.qu.append([data,prior])
        else:
            self.qu.insert(i,[data,prior])

    def dequeue(self):
        if self.qu == []:
            return None
        return self.qu.pop(0)


if __name__ == '__main__':
    print("Queue")
    q = Queue()
    ch = [0]
    while ch[0] != 3:
        ch = list(map(int,input("\n1. enqueue(1 data priority)\n2. dequeue\n3. Exit\nEnter your choice: ").split()))
        if ch[0] == 1:
            q.enqueue(ch[1],ch[2])     #1 is the highest priority
        elif ch[0] == 2:
            print(q.dequeue())
