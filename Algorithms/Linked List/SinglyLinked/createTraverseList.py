class ListNode ():
    def __init__(self, val):
        self.value = val
        self.next = None
    
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
tail = ListNode(5)

head.next = a
a.next = b
b.next = c 
c.next = tail

cur = head    
while cur:
    print(cur.value)
    cur = cur.next
    
    