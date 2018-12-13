from collections import deque
from .. import util


class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, node: 'Node'):
        self.children.append(node)

    def add_metadata(self, metadata: int):
        self.metadata.append(metadata)

    def value(self):
        if not self.children:
            return sum(self.metadata)
        else:
            return sum(self.children[i-1].value() for i in self.metadata
                       if i <= len(self.children))



def sum_of_metadata_entries(list_):
    return parse_node(deque(list_))

def parse_node(d: deque):
    child_node_count = d.popleft()
    metadata_entry_count = d.popleft()
    metadata_sum = 0
    for _ in range(child_node_count):
        metadata_sum += parse_node(d)
    for _ in range(metadata_entry_count):
        metadata_sum += d.popleft()
    return metadata_sum

def value(list_):
    root_node = create_node(deque(list_))
    return root_node.value()

def create_node(d: deque):
    child_node_count = d.popleft()
    metadata_entry_count = d.popleft()
    node = Node()
    for _ in range(child_node_count):
        node.add_child(create_node(d))
    for _ in range(metadata_entry_count):
        node.add_metadata(d.popleft())
    return node


def value_of_node(d: deque):
    child_node_count = d.popleft()
    metadata_entry_count = d.popleft()
    value = 0
    if child_node_count == 0:
        for _ in range(metadata_entry_count):
            value += d.popleft()
            return value
    else:
        for _ in range(child_node_count):
            value += value_of_node(d)



list_ = list(map(int, util.input_lines(8)[0].split()))
print(sum_of_metadata_entries(list_))
print(value(list_))
