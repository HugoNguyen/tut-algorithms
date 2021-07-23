class Node(object):

    def __init__(self, data):
        self.data = data;
        self.height = 0;
        self.leftChild: Node = None;
        self.rightChild: Node = None;

class AVL(object):
    def __init__(self):
        self.root = None;

    def insert(self, data):
        self.root = self.insertNode(data, self.root);

    def insertNode(self, data, node: Node):
        if not node:
            return Node(data);

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild);
        else:
            node.rightChild = self.insertNode(data, node.rightChild);
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

        return self.settleViolation(data, node);

    def settleViolation(self, data, node: Node):

        balance = self.calcBalance(node);

        # case 1 -> left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...");
            return self.rotateRight(node);
        
        # case 2 -> right right heavy situation --> single left rotation
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation...");
            return self.rotateLeft(node);
        
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...");
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node);

        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation...");
            node.rightChild = self.rotateRight(node.rightChild);
            return self.rotateLeft(node);

        return node;

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node: Node):
        if not node:
            return node; # if the tree had just a single node
        
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a left node...")
                del node
                return None

            if not node.leftChild:
                print("Removing a node with a right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with a left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children...")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data;
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        balance = self.calcBalance(node);

        # doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            print("Left left heavy situation...");
            return self.rotateRight(node);
        # left right case
        if balance > 1 and self.calcBalance(node.rightChild) <= 0:
            print("Left right heavy situation...");
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node);
        # right right case
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            print("Right right heavy situation...");
            return self.rotateLeft(node);
        # right left case
        if balance < -1 and self.calcBalance(node.leftChild) >= 0:
            print("Right left heavy situation...");
            node.rightChild = self.rotateRight(node.rightChild);
            return self.rotateLeft(node);

        return node

    def getPredecessor(self, node: Node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

    def calcHeight(self, node: Node):
        if not node:
            return -1;

        return node.height;

    # if return value > 1 its means it is a left heavy tree --> right rotation
    # if return value < -1 its means it is a right heavy tree --> left rotation
    def calcBalance(self, node: Node):
        if not node:
            return 0;

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

    def rotateRight(self, node: Node):
        print("Rotating to the right on node ", node.data);

        tempLeftChild = node.leftChild;
        t = tempLeftChild.rightChild;

        tempLeftChild.rightChild = node;
        node.leftChild = t;

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;

        return tempLeftChild;

    def rotateLeft(self, node: Node):
        print("Rotating to the left on node ", node.data);

        tempRightChild = node.rightChild;
        t = tempRightChild.leftChild;

        tempRightChild.leftChild = node;
        node.rightChild = t;

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;

        return tempRightChild;

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
        print('')

    def traverseInOrder(self, node: Node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        
        print("%s" % node.data, end='\t')

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

# case, Right right heavy situation
# avl = AVL();
# avl.insert(10);
# avl.insert(20);
# avl.insert(30);
# avl.traverse();

# case, Left left heavy situation
# avl = AVL();
# avl.insert(30);
# avl.insert(20);
# avl.insert(10);
# avl.traverse();

# case, Right left heavy situation
# avl = AVL();
# avl.insert(10);
# avl.insert(30);
# avl.insert(20);
# avl.traverse();

# case, Left right heavy situation
# avl = AVL();
# avl.insert(30);
# avl.insert(10);
# avl.insert(20);
# avl.traverse();

# case remove
avl = AVL();
avl.insert(10);
avl.insert(20);
avl.insert(5);
avl.insert(6);
avl.insert(15);

avl.remove(15);
avl.remove(20);
avl.traverse();