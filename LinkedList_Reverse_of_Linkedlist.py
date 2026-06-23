class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
  #Reverse of Linked List
  def reverseList(head):
    prev = None
    curr = head
    while curr:
        nextNode = curr.next    # next ko save karo
        curr.next = prev        # link ulta karo
        prev = curr             # prev ko aage badhao
        curr = nextNode         # curr ko aage badhao
    return prev                 # prev hi naya head hai
