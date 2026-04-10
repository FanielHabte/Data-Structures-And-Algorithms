class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
tail = ListNode(5)

head.next = a
a.next = b
b.next = c
c.next = tail

a.prev = head
b.prev = a
c.prev = b
tail.prev = c

tailPrev = tail.prev 
tailPrev.next = None
tail = tailPrev

cur = head
while cur:
    print(cur.value)
    cur = cur.next
