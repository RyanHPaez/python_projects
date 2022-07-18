class Node:
  def __init__(self, data, reference=None):
    self.data = data
    self.reference = reference

class LinkedList: 
  def __init__(self, head=None):
    self.head = head
  
  def print_linked_list(self):
    if self.head is None:
      print("The linked list is empty")
    #   accessing the nodes
    else:
      c_node = self.head
      while c_node is not None:
        print(c_node.data)
        c_node = c_node.reference

  def add_to_start(self, data):
    n_node = Node(data)
    n_node.reference = self.head
    self.head = n_node

  def add_item(self,data):
    n_node =  Node(data)
    last_node = self.get_last_node()
    print('my last node is ' + str(last_node.data))
    last_node.reference =n_node
   

  def get_last_node (self, ):
    c_node = self.head
    
    while c_node.reference is not None:
        print(f"currect node {c_node.data}")
        c_node = c_node.reference
    if c_node.reference is None:
        return (c_node)


# orginal node
node1 = Node(5)
# print(node1.data)
# print(node1.reference)

# adding a 2nd node
node2 = Node(11)
# print(node2.data)
# print(node2.reference)
# connect the node
node1.reference = node2


# adding node1 in parameter
sl =LinkedList(node1)
sl.print_linked_list()
# print (sl)
# connecting the nodes
node1.reference = node2

node2 = Node(11)
node1.reference = node2
# print(node1.reference)


linked_list1 = LinkedList()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.print_linked_list()

sl.add_to_start(31)

sl.add_item(13)
sl.print_linked_list()
