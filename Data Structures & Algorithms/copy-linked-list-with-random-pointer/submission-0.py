"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        container = []
        cur = head
        while cur:
            container.append(Node(cur.val))
            cur = cur.next
        for i in range(len(container) - 1):
            container[i].next = container[i + 1]
        cur = head
        index = 0
        randomIndex = {}
        while cur:
            randomIndex[cur] = index
            cur = cur.next
            index += 1
        cur = head
        index = 0
        while cur:
            if cur.random:
                container[index].random = container[randomIndex[cur.random]]
            cur = cur.next
            index += 1
        return container[0]