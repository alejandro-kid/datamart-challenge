class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):

        inserted = True

        if self.data == data:
            inserted = False

        elif data < self.data:
            if self.leftChild:
                inserted = self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
        else:
            if self.rightChild:
                inserted = self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)

        return inserted

    def minValueNode(self, node):
        current = node

        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        if self is None:
            return None

        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root) 

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root) 

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        found = False

        if(data == self.data):
            found = True
        elif(data < self.data):
            if self.leftChild:
                found = self.leftChild.find(data)
        else:
            if self.rightChild:
                found = self.rightChild.find(data)
        
        return found


    def inorder(self):
        stack = []
        result = []
        current = self

        while True:
            if current is not None:
                stack.append(current)
                current = current.leftChild
            elif(stack):
                current = stack.pop()
                result.append(current.data)
                current = current.rightChild
            else:
                break

        return result
