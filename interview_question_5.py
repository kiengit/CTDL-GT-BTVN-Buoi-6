class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def get_intersection_node(head1, head2):
  # Function to get the length of a linked list
  def get_length(head):
      length = 0
      while head:
          length += 1
          head = head.next
      return length

  # Get the lengths of both linked lists
  len1 = get_length(head1)
  len2 = get_length(head2)

  # Initialize pointers to the heads of both linked lists
  pointer1, pointer2 = head1, head2

  # Move the pointer of the longer list ahead by the difference in lengths
  while len1 > len2:
      pointer1 = pointer1.next
      len1 -= 1
  while len2 > len1:
      pointer2 = pointer2.next
      len2 -= 1

  # Traverse both lists simultaneously until we find the intersecting node
  while pointer1 and pointer2:
      if pointer1 == pointer2:
          return pointer1
      pointer1 = pointer1.next
      pointer2 = pointer2.next

  # If no intersecting node is found, return None
  return None

# Example usage:
# Create linked list 1: 3 -> 7 -> 8 -> 10
head1 = ListNode(3)
head1.next = ListNode(7)
intersecting_node = ListNode(8)
head1.next.next = intersecting_node
head1.next.next.next = ListNode(10)

# Create linked list 2: 99 -> 1 -> 8 -> 10
head2 = ListNode(99)
head2.next = ListNode(1)
head2.next.next = intersecting_node

# Find the intersecting node
intersection_node = get_intersection_node(head1, head2)

if intersection_node:
  print("Intersection found at node with value:", intersection_node.value)
else:
  print("No intersection found")
