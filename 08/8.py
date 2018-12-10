with open("input1.txt") as file:
    tree_data = [int(x) for x in file.readline().split(" ")]

tree_data_b = tree_data.copy()

# part 1


def parse_node():
    num_children = tree_data.pop(0)
    num_metadata_entries = tree_data.pop(0)
    value = 0
    for x in range(num_children):
        value += parse_node()
    for x in range(num_metadata_entries):
        value += tree_data.pop(0)
    return value


metadata_entries = 0
while tree_data:
    metadata_entries += parse_node()

print(metadata_entries)

# part 2


class Node:
    children = []
    metadata = []

    def __repr__(self):
        return "children {}, metadata {}".format(self.children, self.metadata)

    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def get_value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        value = 0
        for item in self.metadata:
            if 0 < item <= len(self.children):
                value += self.children[item-1].get_value()
        return value


def parse_node_b():
    num_children = tree_data_b.pop(0)
    num_metadata = tree_data_b.pop(0)
    children = []
    metadata = []
    for x in range(num_children):
        children.append(parse_node_b())
    for x in range(num_metadata):
        metadata.append(tree_data_b.pop(0))
    return Node(children, metadata)


parent = parse_node_b()
print(parent.get_value())

