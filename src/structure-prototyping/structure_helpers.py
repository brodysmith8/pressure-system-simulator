from collections import deque


# left-to-right breadth-first traversal
# {p: [c1, c2, c3]}, c1: [c1a, c1b], c2: [c2a, c2b, c2c], c3: []}
def get_structure_tree_bfs(root_structure) -> dict:
    ret = dict()  # parent: [children]
    explored = deque()
    explored.append(root_structure)
    while len(explored) != 0:
        current_parent = explored.popleft()
        children = []
        for child in current_parent.outputs:
            children.append(child)
            explored.append(child)  # this is how we get left-to-right
        ret[current_parent] = children
    return ret


def get_reversed_structure_tree_bfs(root_structure) -> dict:
    ret = dict()  # parent: [children]
    explored = deque()
    explored.append(root_structure)
    while len(explored) != 0:
        current_parent = explored.popleft()
        children = []
        for child in current_parent.inputs:
            children.append(child)
            explored.append(child)  # this is how we get left-to-right
        ret[current_parent] = children
    return ret


# {p: depth, cl:depth, cll:depth, cr, crl, crll, crlr, etc}
def find_structure_depths_dfs(root_structure) -> dict:
    stack = deque()
    queue = deque()
    explored = dict()
    stack.append(root_structure)
    explored[root_structure] = -1
    last_node = root_structure
    while len(stack) != 0:  # while we still have nodes to dive into
        current_node = stack.pop()
        queue = current_node.outputs
        for output in queue:
            if output not in explored:
                last_node = current_node
                explored[output] = explored[last_node]+1
                stack.append(current_node)
                stack.append(output)
                break
    return explored


# left-to-right breadth-first traversal
# {p: [c1, c2, c3]}, c1: [c1a, c1b], c2: [c2a, c2b, c2c], c3: []}
def bfs_get_sublists(li):
    curr = li
    ret = dict()
    next_list = deque()  # use a queue if you wanna do a bfs, stack if dfs
    while True:
        current_parent = curr[0]
        for line in curr:
            if type(line) is str:
                # we are at the first or last element of a subarr
                if current_parent not in ret:  # assumes all element names are unique
                    ret[current_parent] = []
            else:
                # we enter a subarr
                ret[current_parent].append(line[0])
                next_list.append(line)
        if len(next_list) == 0:
            break  # from the while true
        curr = next_list.popleft()
    return ret


# right-to-left depth-first-search
# {p: [c1, c2, c3]}, c1: [c1a, c1b], c2: [c2a, c2b, c2c], c3: []}
def dfs_get_sublists(li):
    curr = li
    ret = dict()
    next_list = deque()  # use a queue if you wanna do a bfs, stack if dfs
    while True:
        current_parent = curr[0]
        for line in curr:
            if type(line) is str:
                # we are at the first or last element of a subarr
                if current_parent not in ret:  # assumes all element names are unique
                    ret[current_parent] = []
            else:
                # we enter a subarr
                ret[current_parent].append(line[0])
                next_list.append(line)
        if len(next_list) == 0:
            break  # from the while true
        curr = next_list.pop()
    return ret
