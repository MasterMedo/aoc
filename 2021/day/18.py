from dataclasses import dataclass


@dataclass
class Node:
    parent: "Node" = None
    val: int = 0
    left: "Node" = None
    right: "Node" = None

    @classmethod
    def from_list(cls, element, parent=None):
        if isinstance(element, int):
            return Node(parent=parent, val=element)

        left, right = element
        node = Node(parent=parent)
        node.left = Node.from_list(left, parent=node)
        node.right = Node.from_list(right, parent=node)
        return node

    def __add__(self, other):
        snail = Node(left=self, right=other)
        snail.left.parent = snail
        snail.right.parent = snail
        snail.explode()
        while snail.split():
            snail.explode()

        return snail

    def explode(self, depth=0):
        if self.left is None and self.right is None:
            return

        if depth >= 4:
            self.parent.add_left(self.left.val, self, True)
            self.parent.add_right(self.right.val, self, True)
            self.val = 0
            self.left = None
            self.right = None
            return

        self.left.explode(depth + 1)
        self.right.explode(depth + 1)

    def split(self):
        if self.val > 9:
            left = self.val // 2
            right = self.val - left
            self.left = Node(parent=self, val=left)
            self.right = Node(parent=self, val=right)
            self.val = 0
            return True

        if self.left is not None:
            if self.left.split():
                return True

        if self.right is not None:
            if self.right.split():
                return True

        return False

    def add_right(self, val, child, right=False):
        if right:
            if self.right is None or self.right is child:
                if self.parent is not None:
                    self.parent.add_right(val, self, True)
                return

            self.right.add_right(val, self)
            return

        if self.left is None:
            self.val += val
        else:
            self.left.add_right(val, self)

    def add_left(self, val, child, left=False):
        if left:
            if self.left is None or self.left is child:
                if self.parent is not None:
                    self.parent.add_left(val, self, True)
                return

            self.left.add_left(val, self)
            return

        if self.right is None:
            self.val += val
        else:
            self.right.add_left(val, self)

    def magnitude(self):
        if self.left is None and self.right is None:
            return self.val

        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return f"[{repr(self.left)}, {repr(self.right)}]"


with open("../input/18.txt") as f:
    snails = list(map(eval, f.read()[:-1].split("\n")))

snail = Node.from_list(snails[0])
for other in snails[1:]:
    snail += Node.from_list(other)

print(snail.magnitude())

max_magnitude = 0
for i in range(len(snails)):
    for j in range(len(snails)):
        if i != j:
            snail = Node.from_list(snails[i]) + Node.from_list(snails[j])
            max_magnitude = max(max_magnitude, snail.magnitude())

print(max_magnitude)
