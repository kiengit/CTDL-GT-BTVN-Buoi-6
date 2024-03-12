class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def delete_duplicates(head):
  current_node = head

  while current_node and current_node.next:
      if current_node.value == current_node.next.value:
          current_node.next = current_node.next.next
      else:
          current_node = current_node.next

  return head

def print_list(head):
  result = []
  while head:
      result.append(head.value)
      head = head.next
  print(result)

# Example usage:
# Create the sorted linked list
head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(2)

head2 = ListNode(1)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(3)
head2.next.next.next.next = ListNode(3)

# Print original lists
print("Original list 1:")
print_list(head1)
print("Original list 2:")
print_list(head2)

# Delete duplicates
head1 = delete_duplicates(head1)
head2 = delete_duplicates(head2)

# Print lists after deleting duplicates
print("List 1 after deleting duplicates:")
print_list(head1)
print("List 2 after deleting duplicates:")
print_list(head2)
