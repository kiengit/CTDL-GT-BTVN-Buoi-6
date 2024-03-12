class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def add_two_numbers(l1, l2):
  dummy_head = ListNode()
  current_node = dummy_head
  carry = 0

  while l1 or l2 or carry:
      # Calculate sum of current digits along with carry
      sum_val = carry
      if l1:
          sum_val += l1.value
          l1 = l1.next
      if l2:
          sum_val += l2.value
          l2 = l2.next

      # Update carry for next calculation
      carry = sum_val // 10
      sum_val %= 10

      # Create a new node with the sum value
      current_node.next = ListNode(sum_val)
      current_node = current_node.next

  return dummy_head.next

def print_list(head):
  result = []
  while head:
      result.append(head.value)
      head = head.next
  print(result)

# Example usage:
# Create linked list for number 342 (in reverse order: 2 -> 4 -> 3)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create linked list for number 465 (in reverse order: 5 -> 6 -> 4)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Print original lists
print("Number 1 (reversed):")
print_list(l1)
print("Number 2 (reversed):")
print_list(l2)

# Add the two numbers
sum_list = add_two_numbers(l1, l2)

# Print sum as a linked list
print("Sum of the two numbers (reversed):")
print_list(sum_list)
