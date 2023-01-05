from structure_helpers import get_structure_tree_bfs, get_reversed_structure_tree_bfs, find_structure_depths_dfs
from create_topology import Topology
# from pptree import print_tree  # external dependency for printing the structure tree


topo = Topology()
root = topo.get_root()
last = topo.get_last_leaf()
forward_tree = get_structure_tree_bfs(root)
print(find_structure_depths_dfs(root))
reverse_tree = get_reversed_structure_tree_bfs(last)

# print('Forward Tree:')
# print_tree(root, 'outputs')
# print('\nReverse Tree:')
# print_tree(last, 'inputs')

# preprocess phase 1
