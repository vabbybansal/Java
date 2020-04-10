# Reverse a linked list from position m to n. Do it in one-pass.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.end = None

    def addNode(self, x):
        node = ListNode(x)
        if self.head == None:
            self.head = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
    def __repr__(self):
        temp = self.head
        printStr = ''
        while temp != None:
            printStr += '->' + str(temp.val)
            temp = temp.next
        return printStr

ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.addNode(5)
ll.addNode(6)

print ll

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            return head

        count = 1
        temp = head
        while True:
            if count+1 == m or count == m:
                break
            count += 1
            temp = temp.next
        if m != 1:
            startBefore = temp
            start = temp.next
            temp = temp.next
            tempNext = temp.next
        else:
            start = temp
            tempNext = temp.next
            count -= 1

        while count < n-1:
            count += 1
            tempNextNext = tempNext.next
            tempNext.next = temp
            temp = tempNext
            tempNext = tempNextNext

        if m == 1:
            head = temp
            start.next = tempNext
        else:
            startBefore.next = temp
            start.next = tempNext

        return head

obj = Solution()
# obj.reverseBetween(ll.head, 3, 5)
# obj.reverseBetween(ll.head, 3, 6)
ll.head = obj.reverseBetween(ll.head, 1, 6)
# obj.reverseBetween(ll.head, 1, 5)
print ll