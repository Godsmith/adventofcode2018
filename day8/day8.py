from collections import deque


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