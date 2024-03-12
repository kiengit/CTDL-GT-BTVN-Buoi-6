class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def insert_at_beginning(self, value):
      new_node = Node(value)
      new_node.next = self.head
      self.head = new_node

  def print_list(self):
      current_node = self.head
      while current_node:
          print(current_node.value, end=" -> ")
          current_node = current_node.next
      print("None")

# Example Usage:
my_list = LinkedList()
my_list.insert_at_beginning(10)
my_list.insert_at_beginning(20)
my_list.insert_at_beginning(30)
my_list.print_list()
