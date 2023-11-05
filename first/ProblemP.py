from collections import deque
from dataclasses import dataclass, field
from heapq import heapify, heappush, heappop
from typing import Optional


@dataclass(order=True)
class Tree:
    val: int
    left: Optional['Tree'] = field(default=None, compare=False)
    right: Optional['Tree'] = field(default=None, compare=False)
    leaf: bool = field(init=False)

    def __post_init__(self):
        self.leaf = not self.left and not self.right


input()
heap = list(map(Tree, map(int, input().split())))
heapify(heap)

while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    tree = Tree(a.val + b.val, a, b)
    heappush(heap, tree)

queue = deque(heap)
layer, k = 0, 0
while queue:
    n = len(queue)
    for _ in range(n):
        node = queue.popleft()

        if node.leaf:
            k += layer
            continue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    layer += 1
print(k)
