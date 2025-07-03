class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node1 = Node(value)
        self.head = node1
        self.tail = node1
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    def append(self, value):   
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return temp.value
        else:
            pre = temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            pre.next = None
            self.tail = pre
            self.length -= 1
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index not in range(0, self.length):
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        if index not in range(0, self.length):
            return None
        current = self.head
        for i in range(index):
            current = current.next

        current.value = value

    def set_value_2(self,index,value):
        temp = self.get(index)
        
        if temp:
            temp.value = value
    
    def insert(self, index, value):
        if index not in range(0, self.length+1):
            return False
        
        if index == 0:
            self.prepend(value)
            return True
        
        else:
            new_node = Node(value)
            temp = self.get(index)
            current = self.head

            for _ in range(index-1):
                current = current.next

            current.next = new_node
            new_node.next = temp
            self.length += 1
            return True

    def remove(self,index):

        if index not in range(0,self.length):
            return False
        if index == 0:
            self.pop_first()
            return True
        elif index == self.length - 1:
            self.pop()
            return True
        
        before = self.get(index-1)
        to_remove = before.next

        before.next = to_remove.next
        to_remove.next = None
        self.length -= 1
        return True
    
    def reverse(self):
        if self.head is None:
            return False
        if self.length == 1:
            return True
        
        current = self.head
        self.head, self.tail = self.tail, self.head
        before = None


        while current:
            after = current.next
            current.next = before
            before = current
            current = after
        
        return True
            
