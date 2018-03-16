# reverse a singly linked list


# iterative solution
class Solution(object):
  def reverseList(self, head):
    if head is None:
      return head
    
    curr = head
    prev = None
    
    while curr:
      nxt = curr.next_node
      curr.next = prev
      
      prev = curr
      curr = nxt
    return prev


# recursive solution
class recSolution(object):
  def reverseList2(head):
    if head is null or head.next_node = null:
      return head
    p = reverseList2(head.next_node)
    head.next_node.next_node = head
    head.next_node = null
    return p
      

