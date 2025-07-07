class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:

        if self.size >= self.capacity:
            return False

        nt_node = self.head.next

        new_Node = ListNode(value)
        new_Node.next = nt_node
        nt_node.prev = new_Node
        self.head.next = new_Node
        new_Node.prev = self.head

        self.size += 1
        print("enqueue", self.size)

        return True

    def deQueue(self) -> bool:
        print("dequeue - size", self.size)

        if self.size == 0:
            return False

        delete_node = self.tail.prev
        prev_del_node = delete_node.prev
        prev_del_node.next = self.tail
        self.tail.prev = prev_del_node

        del delete_node
        self.size -= 1
        return True

    def Front(self) -> int:

        cur = self.tail
        while cur:
            print(cur.val)
            cur = cur.prev

        return self.tail.prev.val

    def Rear(self) -> int:
        return self.head.next.val

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.capacity else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
