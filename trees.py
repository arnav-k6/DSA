
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self,value):
        new_node = Node(value)
        self.root = new_node


    def insert(self,value):    
        new_node = Node(value)
        temp = self.root
        inserted = False
        if not self.root:
            self.root = new_node
            return True
        
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
    def contains(self,value):
        if not self.root:
            return False
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            else:
                return True
            
        return False
    
    def maxValue(self,root):
        if not root:
            return
        leftval = self.maxValue(root.left)
        rightval = self.maxValue(root.right)
        return max(leftval,rightval,root)

myTree = BinarySearchTree(10)
myTree.insert(5)
myTree.insert(15)
myTree.insert(3)
myTree.insert(7)
myTree.insert(12)
myTree.insert(18)

print(myTree.root.value)        # 10
print(myTree.root.left.value)   # 5
print(myTree.root.right.value)  # 15
print(myTree.root.left.left.value)   # 3
print(myTree.root.left.right.value)  # 7
print(myTree.root.right.left.value)  # 12
print(myTree.root.right.right.value) 
print("Max Value in Tree: " + myTree.maxValue(myTree))
