
class Node():
    def __init__(self, parent, value=None):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self.is_leaf():
            return str(self.value)
        return f"[{self.left},{self.right}]"

    def magnitude(self):
        if self.is_leaf():
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def add_child(self, node):
        if not self.left:
            self.left = node
        elif not self.right:
            self.right = node
        else:
            raise ValueError("Left and right already assigned")

    def is_leaf(self):
        return not self.left and not self.right

    def get_prev(self):
        n = self
        while True:
            if n.parent is None:
                return None
            if n == n.parent.right:
                break
            n = n.parent
        n = n.parent.left
        # get rightmost child
        while n.right is not None:
            n = n.right
        return n

    def get_next(self):
        n = self
        while True:
            if n.parent is None:
                return None
            if n == n.parent.left:
                break
            n = n.parent
        n = n.parent.right
        # get leftmost child
        while n.left is not None:
            n = n.left
        return n

    def explode(self):
        # add left and right values
        prev_num = self.get_prev()
        if prev_num:
            prev_num.value += self.left.value
        next_num = self.get_next()
        if next_num:
            next_num.value += self.right.value
        # replace with 0
        self.value = 0
        self.left = None
        self.right = None

    def split(self):
        left_val = right_val = self.value // 2
        if self.value % 2 == 1:
            right_val += 1
        self.value = None
        self.left = Node(self, left_val)
        self.right = Node(self, right_val)


def parse_sf_num(text):
    # start stack with root node
    assert text[0] == "["
    root = Node(None)
    stack = [root]
    # parse remaining text
    for c in text[1:]:
        if c == "[":
            p = stack[-1]
            n = Node(p)
            p.add_child(n)
            stack.append(n)
        elif c == "]":
            stack.pop()
        elif c.isdigit():
            p = stack[-1]
            n = Node(p, int(c))
            p.add_child(n)
    if len(stack) > 0:
        raise ValueError("Too few closing brackets")
    return root


def read_input():
    with open("input.txt") as f:
        text = f.read().strip()
    return text.split("\n")


def find_depth_four(node, depth):
    if node.is_leaf():
        return None
    if depth == 4:
        return node
    left = find_depth_four(node.left, depth + 1)
    if left:
        return left
    right = find_depth_four(node.right, depth + 1)
    if right:
        return right
    return None


def find_over_nine(node):
    if node.is_leaf():
        if node.value > 9:
            return node
        return None
    left = find_over_nine(node.left)
    if left:
        return left
    right = find_over_nine(node.right)
    if right:
        return right
    return None


def reduce_sf_num(sfn):
    while True:
        node = find_depth_four(sfn, 0)
        if node:
            node.explode()
            continue
        node = find_over_nine(sfn)
        if node:
            node.split()
            continue
        break


def add_sf_nums(left, right):
    node = Node(None)
    left.parent = node
    right.parent = node
    node.left = left
    node.right = right
    reduce_sf_num(node)
    return node


def part1():
    lines = read_input()
    sf_nums = [parse_sf_num(line) for line in lines]
    result = sf_nums.pop(0)
    for sfn in sf_nums:
        result = add_sf_nums(result, sfn)
    return result.magnitude()


def part2():
    lines = read_input()
    largest = -1
    for x in lines:
        for y in lines:
            if x == y:
                continue
            left = parse_sf_num(x)
            right = parse_sf_num(y)
            mag = add_sf_nums(left, right).magnitude()
            if mag > largest:
                largest = mag
    return largest


if __name__ == "__main__":
    print("Part 1:")
    print(part1())
    print("Part 2:")
    print(part2())
