class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

# head -> 3 -> 5 -> 6 -> tail

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.hash_map = {}  # key = int val = Node

    def get(self, key: int) -> int:

        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        prev_node = node.prev
        next_node = node.nxt

        prev_node.nxt = next_node
        next_node.prev = prev_node

        first_node = self.head.nxt

        self.head.nxt = node
        node.nxt = first_node
        node.prev = self.head
        first_node.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:

            node = self.hash_map[key]
            # update the value
            node.val = value

            # move the node the latest

            prev_node = node.prev
            next_node = node.nxt

            prev_node.nxt = next_node
            next_node.prev = prev_node

            first_node = self.head.nxt

            self.head.nxt = node
            node.nxt = first_node
            node.prev = self.head
            first_node.prev = node

        else:

            new_node = Node(key, value)
            self.hash_map[key] = new_node

            # insert node at the front
            first_node = self.head.nxt

            self.head.nxt = new_node
            new_node.nxt = first_node
            new_node.prev = self.head
            first_node.prev = new_node

            if len(self.hash_map) > self.capacity:
                remove_node = self.tail.prev
                del self.hash_map[remove_node.key]

                prev_node = remove_node.prev
                prev_node.nxt = self.tail
                self.tail.prev = prev_node
