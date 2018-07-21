class Node():

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree():

    def __init__(self,data=None):
        self.root = Node(data)

    def insert(self,data):
        #self.__insert(tmp,data)
        if self.root.data == None:
            self.root.data = data
        else:
            preptr = None
            ptr = self.root
            while(ptr != None):
                preptr = ptr
                if data < ptr.data:
                    ptr = ptr.left
                else:
                    ptr = ptr.right
            if data < preptr.data:
                preptr.left = Node(data)
            else:
                preptr.right = Node(data)

    def delete(self,data):
        if self.root.data == None:                  #if tree is null
            return False
        preptr = None                               #parent of node to be deleted
        ptr = self.root                             #the node to be deleted
        while (ptr != None and ptr.data != data):   #traverse to find the node or until the node is not found
            preptr = ptr
            if data < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        if ptr == None:                             #node not found
            return False
        elif ptr.right == None:                     #node has only one child
            if preptr.right == ptr:
                preptr.right = ptr.left
            else:
                preptr.left = ptr.left
            del(ptr)
            return True
        elif ptr.left == None:                      #node has only on child
            if preptr.right == ptr:
                preptr.right = ptr.right
            else:
                preptr.left = ptr.right
            del(ptr)
            return True
        else:                                       #node has 2 child
            preln = ptr
            ln = ptr.left
            while(ln.right != None):                #findlargestNode
                preln = ln
                ln = ln.right
            ptr.data = ln.data
            preln.right = None
            del(ln)
            return True




    def search(self,data):
        tree = self.__search(self.root,data)
        if tree.data == None:
            return False
        else:
            return True

    def __search(self,tree,data):
        if tree == None or tree.data == data:
            return tree
        else:
            if data < tree.data:
                return self.__search(tree.left,data)
            else:
                return self.__search(tree.right,data)

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self,tree):
        if tree != None:
            self.__inorder(tree.left)
            print(tree.data,end=" ")
            self.__inorder(tree.right)

    def postorder(self):
        self.__postorder(self.root)
        print()

    def __postorder(self,tree):
        if tree != None:
            self.__postorder(tree.left)
            self.__postorder(tree.right)
            print(tree.data,end=" ")

    def preoder(self):
        self.__preorder(self.root)
        print()

    def __preorder(self,tree):
        if tree != None:
            print(tree.data,end=" ")
            self.__preorder(tree.left)
            self.__preorder(tree.right)

    def levelorder(self):
        self.__levelorder(self.root)
        print()

    def __levelorder(self,tree):
        q=[tree]
        while(q!=[]):
            tmp = q.pop(0)
            print(tmp.data,end=" ")
            if tmp.left != None:
                q.append(tmp.left)
            if tmp.right != None:
                q.append(tmp.right)




t = Tree()
t.insert(45)
t.insert(39)
t.insert(56)
t.insert(54)
t.insert(78)
t.insert(55)
t.insert(80)
#t.inorder()
#t.preoder()
#t.postorder()
t.delete(56)
t.levelorder()
#print(t.search(3))
