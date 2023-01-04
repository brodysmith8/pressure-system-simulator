from structure_helpers import get_structure_tree_bfs
from create_topology import create_topology

root = create_topology()

print(get_structure_tree_bfs(root))
