from treelib import Tree
import os

def build_tree(path: str, tree: Tree, parent: str = None, max_depth: int = 3, level: int = 0):
    if level > max_depth:
        return
    for item in sorted(os.listdir(path)):
        if item in ["__pycache__", ".git", ".idea", ".venv"]:
            continue
        full_path = os.path.join(path, item)
        node_id = os.path.relpath(full_path, start=root)
        tree.create_node(tag=item, identifier=node_id, parent=parent)
        if os.path.isdir(full_path):
            build_tree(full_path, tree, parent=node_id, max_depth=max_depth, level=level+1)

root = "."
tree = Tree()
tree.create_node(tag=os.path.basename(os.path.abspath(root)) or "project", identifier=root)
build_tree(root, tree, parent=root, max_depth=3)


tree.show()