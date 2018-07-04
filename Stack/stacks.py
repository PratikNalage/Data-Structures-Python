class Stack():
    '''An ADT for stact'''
    def __init__(self):
        self.st = []
        self.top = -1

    def push(self,data):
        self.st.append(data)
        self.top += 1

    def pop(self):
        self.top -= 1
        if self.top < 0:
            return None
        return self.st.pop()

    def peek(self):
        if self.top < 0:
            return None
        return self.st[self.top]

if __name__ == '__main__':
    print("STACK")
    s = Stack()
    ch = [0]
    while ch[0] != 4:
        ch = list(map(int,input("\n1. Push(1 data)\n2. Pop\n3. Peek\n4. Exit\nEnter your choice: ").split()))
        if ch[0] == 1:
            s.push(ch[1])
        elif ch[0] == 2:
            print(s.pop())
        elif ch[0] == 3:
            print(s.peek())
