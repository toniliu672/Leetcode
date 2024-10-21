class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_to_node = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            if self.head.next.count != 1:
                self._add_node_after(Node(1), self.head)
            self.head.next.keys.add(key)
            self.key_to_node[key] = self.head.next
        else:
            node = self.key_to_node[key]
            next_node = node.next
            if next_node.count != node.count + 1:
                self._add_node_after(Node(node.count + 1), node)
            next_node = node.next
            next_node.keys.add(key)
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)
            self.key_to_node[key] = next_node

    def dec(self, key: str) -> None:
        node = self.key_to_node[key]
        if node.count == 1:
            del self.key_to_node[key]
        else:
            prev_node = node.prev
            if prev_node.count != node.count - 1:
                self._add_node_after(Node(node.count - 1), prev_node)
            prev_node = node.prev
            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node
        node.keys.remove(key)
        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""

    def _add_node_after(self, new_node, node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev