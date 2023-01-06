import structure_helpers as sh
from create_topology import Topology
from pptree import print_tree  # external dependency for printing the structure tree

# preprocess
topo = Topology()
root = topo.get_root()
last = topo.get_last_leaf()
forward_tree = sh.get_structure_tree_bfs(root)
depths = sh.find_structure_depths_dfs(root)
sh.calculate_nodal_volumes_by_depth(depths)

# pressurize
sh.pressurize(root)

print('\nEnd of Preprocessing Stage\n')

# result
print('Forward Tree:')
print_tree(root, 'outputs')
print('Reverse Tree:')
print_tree(last, 'inputs')
