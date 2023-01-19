#implementation of the doubly linked list
#@todo: remove print for error traces


class Node():

    def __init__(self, data):
        self.item = data    
        self.next = None    
        self.previous = None

class DoublyLinkedList:    
    def __init__(self):
        self.start_node = None 
        self.header = 0  

    #Iterator Function
    def __iter__(self): 
         node = self.start_node
         while node:
            yield node
            node = node.next
            if not node:
                break
             
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.header = 1
        else:
            raise DLLException("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            self.insert_in_emptylist(data)
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.previous = new_node
        self.start_node = new_node
        self.header += 1

    def insert_at_end(self, data):
        if self.start_node is None:
            self.insert_in_emptylist(data)
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.previous = n
        self.header += 1

    def delete_at_start(self):
        if self.start_node is None:
            self.header = 0
            raise DLLException("The list has no element to delete")
        if self.start_node.next is None:
            self.start_node = None
            self.header = 0
            return
        self.start_node = self.start_node.next
        self.start_prev = None
        self.header -= 0
        

    def delete_at_end(self):
        if self.start_node is None:
            self.header = 0
            raise DLLException("The list has no element to delete")
            #return 
        if self.start_node.next is None:
            self.start_node = None
            self.header = 0
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.previous.next = None
        self.header -= 0

    def traverse_list(self):
        if self.start_node is None:
            raise DLLException("List has no element")
            #return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.next

    def search_list(self, search_item):
        position = 0
        results = []
        if self.start_node is None:
            raise DLLException("List has no element")
        else:
            n = self.start_node
            while n is not None:
                position += 1
                if n.item == search_item:
                    results.append(position)
                n = n.next
        return results

    def search_list_previous(self, search_item):
        position = 0
        results = []
        if self.start_node is None:
            raise DLLException("List has no element")
        else:
            n = self.start_node
            while n is not None:
                position += 1
                if n.item == search_item:
                    results.append(n.previous)
                n = n.next
        return results

    def reverse_linked_list(self):
        if self.start_node is None:
            raise DLLException("Empty lists cannot be reversed")
        p = self.start_node
        q = p.next
        p.next = None
        p.previous = q
        while q is not None:
            q.previous = q.next
            q.next = p
            p = q
            q = q.previous
        self.start_node = p

    def setdir(self, data, left, right):
        if self.start_node is None:
            new_node = Node(data)
            new_node.next = left
            new_node.previous = right
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.previous = new_node
        self.start_node = new_node

class DLLException(Exception):
    pass