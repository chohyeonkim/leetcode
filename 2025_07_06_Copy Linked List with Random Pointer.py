"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# create copies of all the nodes
# store the address of the copies of those random pointers
# hash map original nodes - corresponding copies
# dummy -> * *
#          ! !


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if not head:
            return None

        node_map = {}

        cur = head

        while cur:
            val = cur.val
            new_node = Node(val)  # nextNode, randomNode = None
            node_map[cur] = new_node

            print("cur", cur.val)
            print("cur", cur.next)
            print("cur", cur.random)

            cur = cur.next

        cur = head
        while cur:
            copy_node = node_map[cur]

            if not cur.next:
                next_node = None
            else:
                next_node = node_map[cur.next]

            if not cur.random:
                random_node = None
            else:
                random_node = node_map[cur.random]

            # link next node
            copy_node.next = next_node
            # link random node
            copy_node.random = random_node

            cur = cur.next

        return node_map[head]
