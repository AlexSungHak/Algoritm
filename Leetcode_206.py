#Leetcode 206 Reverse Linked list
#input: [1, 2, 3, 4, 5] / output: [5, 4, 3, 2, 1]

def reverseList(self, head):
    if not head or not head.next:
        return head
    
    curr = head.next
    reverse = self.reverseList(curr)
    curr.next = head
    head.next = None

    return reverse