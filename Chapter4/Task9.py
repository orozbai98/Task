# бинарный поиск дерева 


class BTree(object):
    def __init__(self, data):
        self.data = data
        self.rChild = None
        self.lChild = None

    def __str__(self):
        return (self.lChild.__str__() + '<-' if self.lChild != None else '') + \
               self.data.__str__() + ('->' + self.rChild.__str__()
                                      if self.rChild != None else '')

    def insert(self, btree):
        if self.data > btree.data: #insert left
            if self.lChild == None:
                self.lChild = btree
            else:
                self.lChild.insert(btree)
        else: #insert right
            if self.rChild == None:
                self.rChild = btree
            else:
                self.rChild.insert(btree)

# root = Node(50)
# root = root.addNode(30)
# root = root.addNode(20)
# root = root.addNode(40)
# root = root.addNode(70)
# root = root.addNode(60)
# root = root.addNode(80)

def main():
    btreeRoot = BTree(50)
    print('inserted %s:' %50, btreeRoot)

    btreeRoot.insert(BTree(30))
    print('inserted %s:' %30, btreeRoot)

    btreeRoot.insert(BTree(20))
    print('inserted %s:' %20, btreeRoot)

    btreeRoot.insert(BTree(40))
    print('inserted %s:' %40, btreeRoot)

    btreeRoot.insert(BTree(70))
    print('inserted %s:' %70, btreeRoot)

    btreeRoot.insert(BTree(60))
    print('inserted %s:' %60, btreeRoot)

    btreeRoot.insert(BTree(80))
    print('inserted %s:' %80, btreeRoot)
main()










