from collections import deque
from typing import Dict
from structure import Structure


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
                # print(f'   -> Output: {output}')
                last_node = current_node
                explored[output] = explored[last_node]+1
                stack.append(current_node)
                stack.append(output)
                break
    return explored


def calculate_nodal_volumes_by_depth(depths: Dict[Structure, int]) -> None:
    by_level = dict()
    for key in depths:
        if depths[key] not in by_level:
            by_level[depths[key]] = [key]
        else:
            by_level[depths[key]].append(key)

    # lol
    for key in sorted(list(by_level))[::-1]:
        for child in by_level[key]:
            for parent in child.inputs:
                parent.add_downstream_nodal_volume(child)


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


# pressurizes the system in-place
# since we have the entire initial volume load for the system
# calculated in the preprocess phase, then we can immediately calculate
# the pressure required to sate that. How will pressure regulators work?
# Well, if the required downstream volume load is higher than the output
# pressure of the pressure regulator, then the required volume won't be delivered.
# Possibly, add a plausibility check using the sum of the system pressures and the
# downstream volume requirements of each pressure-limiting device (i.e. only regulators,
# for now) to see if downstream vol can be met, and give a warning if not?

# bfs p_in = p_out from parent / # parent's outputs
def pressurize(root_structure) -> None:
    stack = deque()
    queue = deque()
    storage_vessels = set()
    explored = dict()
    stack.append(root_structure)
    explored[root_structure] = -1
    last_node = root_structure

    running_sum_n: float = 0.0
    for storage_vessel in root_structure.outputs:
        storage_vessels.add(storage_vessel)
        p = 100.0*1000.0*storage_vessel.internal_pressure
        v = storage_vessel.internal_volume.total()
        print(f'Vessel: {storage_vessel},\np: {p} bar,\nV: {v} m3\nn: {p*v / (8.314*(25.0 + 273.15))}')
        running_sum_n += p*v / (8.314*(25.0 + 273.15))

    initial_v = running_sum_n
    while len(stack) != 0:  # while we still have nodes to dive into
        current_node = stack.pop()
        if current_node not in storage_vessels:
            p: float = current_node.internal_pressure
            v: float = current_node.internal_volume.total()
            pv_div_rt = 100.0*1000.0*p*v / (8.314*(25.0 + 273.15))
            running_sum_n -= pv_div_rt
            if running_sum_n < 0:
                print("!!!OUT OF GAS!!!")

            s1 = f'Current Node: {current_node}, '
            s2 = f'\n  internal_pressure: {p} bar, '
            s3 = f'\n  (P*V_internal)/RT = {pv_div_rt} mol, '
            s4 = f'\nRemaining n: {running_sum_n} mol\n'
            print(f'{s1}{s2}{s3}{s4}')
        queue = current_node.outputs
        for output in queue:
            if output not in explored:
                # print(f'   -> Output: {output}')
                # pressurize
                if not current_node.is_root:
                    output.set_pressure(current_node.pressure_out)
                last_node = current_node
                explored[output] = explored[last_node]+1
                stack.append(current_node)
                stack.append(output)
                break
    eqm_str = f'{initial_v/(initial_v-running_sum_n)} simulation timesteps'
    print(f'How long can this demand be met? (i.e. how long until equilibrium?): {eqm_str}')
