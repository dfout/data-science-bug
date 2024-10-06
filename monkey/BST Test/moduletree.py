class TreeNode:
    def __init__(self, key):
        self.key = key
        self.count = 1  
        self.left = None
        self.right = None

class ProductIDBST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if node is None:
            return TreeNode(key)
        if key == node.key:
            node.count += 1 
        elif key < node.key:
            node.left = self._insert_recursively(node.left, key)
        else:  # key > node.key
            node.right = self._insert_recursively(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:
            return None
        if key == node.key:
            if node.count > 1:
                node.count -= 1  
                return node
            else:  
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.count = temp.count
                temp.count = 1  
                node.right = self._delete_recursively(node.right, temp.key)
        elif key < node.key:
            node.left = self._delete_recursively(node.left, key)
        else:  # key > node.key
            node.right = self._delete_recursively(node.right, key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, key):
        return self._find_recursively(self.root, key)

    def _find_recursively(self, node, key):
        if node is None or key == node.key:
            return node
        if key < node.key:
            return self._find_recursively(node.left, key)
        return self._find_recursively(node.right, key)