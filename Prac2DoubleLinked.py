# DoubleLinked List
class Node: 
   def _init_(self, data):                            
     self.item=data
     self.ref = None

class LinkedList: 
    def _init_(self):         
        self.start_node=None

def insert_at_start(self, data): 
    new_node = Node(data)
    new_node.ref = self.start_node
    self.start_node= new_node


def delete_at_start(self): 
    if self.start_node is None:
     print("The list has no element to delete") 
    return
    self.start_node = self.start_node.ref


def search_item(self, x): 
     if self.start_node is None: print("List has no elements")
     return 
    n = self.start_node while n is not None:
 if n.item == x:print("Item found") 
   return True 
    n = n.ref  
print("item not found") 
 return False

def reverse_linkedlist(self): prev = None
 n = self.start_node 
while n is not None:
   next = n.ref 
    n.ref = prev prev = n
    n = next 
    self.start_node = prev

new_linked_list = LinkedList()

new_linked_list.insert_at_start(20)


new_linked_list.search_item(5)

new_linked_list.delete_at_start()


new_linked_list.reverse_linkedlist()


Try it in another File
def merge_lists(head1, head2): 
if head1 is None and head2 is None: 
return None 
if head1 is None: 
return head2 if head2 is None: return head1 
if head1.value < head2.value: 
temp = head1 
else: temp = head2
 while head1 != None and head2 != None: 
if head1.value < head2.value: 
temp.next = head1 
head1 = head1.next 
else: 
temp.next = head2 
head2 = head2.next 
if head1 is None: 
temp.next = head2 
else: 
temp.next = head1
return temp 
pass
