"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def reset_links(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_head = ListNode(value)
        self.length+=1
        if self.head:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head
        else:
            self.head = new_head
            self.tail = new_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        old_head = self.head.value
        self.delete(self.head)
        return old_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_tail = ListNode(value)
        self.length+=1
        if self.tail:
            self.tail.next = new_tail
            new_tail.prev = self.tail
        else:
            self.head = new_tail
        
        self.tail = new_tail   

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        
        #if list is empty
        if not self.head:
            print("Empty")
            return
        
        self.length-=1
        #if list has just one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        #More than one node, but current node is head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        #More than one node, node to be deleted is tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.reset_links()
    
    def printMiddle(self): 
        slow_ptr = self.head 
        fast_ptr = self.head 
  
        if self.head is not None: 
            while (fast_ptr.next is not None and fast_ptr.next.next is not None): 
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.value) 
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        highest = self.head.value
        curr_node = self.head
        for _ in range(self.length):
            if curr_node.next:
                if curr_node.value > highest:
                    highest = curr_node.value
                    curr_node = curr_node.next
                else:
                    curr_node = curr_node.next
            else:
               if curr_node.value > highest:
                    highest = curr_node.value 
        return highest
        
    
    
        