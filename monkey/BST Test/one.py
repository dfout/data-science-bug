import unittest
from moduletree import TreeNode, ProductIDBST  # Replace your_module

class TestProductIDBST(unittest.TestCase):

    def setUp(self):
        self.bst = ProductIDBST()

    def test_insert_empty_tree(self):
        self.bst.insert(10)
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.count, 1)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)

    def test_insert_unique_keys(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.right.key, 15)
        self.assertEqual(self.bst.root.count, 1)
        self.assertEqual(self.bst.root.left.count, 1)
        self.assertEqual(self.bst.root.right.count, 1)

    def test_insert_duplicate_keys(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(10)
        self.bst.insert(10)
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.count, 3)
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertEqual(self.bst.root.left.count, 1)


    def test_delete_node_no_children(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.delete(5)
        self.assertEqual(self.bst.root.left, None)
        self.bst.delete(15)
        self.assertEqual(self.bst.root.right, None)

    def test_delete_node_one_child(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(12)
        self.bst.delete(15)
        self.assertEqual(self.bst.root.right.key, 12)
        self.bst.delete(12)
        self.assertEqual(self.bst.root.right, None)

    def test_delete_node_two_children(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(12)
        self.bst.insert(18)
        self.bst.delete(15)
        self.assertEqual(self.bst.root.right.key, 18)
        self.assertEqual(self.bst.root.right.left.key, 12)
        self.assertEqual(self.bst.root.right.count, 1)



    def test_delete_non_existent_key(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.delete(20)  # Non-existent key
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.left.key, 5)
        self.assertIsNone(self.bst.root.right)


    def test_delete_duplicate_keys(self):
        self.bst.insert(10)
        self.bst.insert(10)
        self.bst.insert(10)
        self.bst.delete(10)
        self.assertEqual(self.bst.root.count, 2)
        self.bst.delete(10)
        self.assertEqual(self.bst.root.count, 1)
        self.bst.delete(10)
        self.assertIsNone(self.bst.root)


    def test_find_empty_tree(self):
        self.assertIsNone(self.bst.find(10))

    def test_find_existing_key(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.find(10).key, 10)
        self.assertEqual(self.bst.find(5).key, 5)
        self.assertEqual(self.bst.find(15).key, 15)

    def test_find_non_existent_key(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertIsNone(self.bst.find(20))
        self.assertIsNone(self.bst.find(1))




if __name__ == '__main__':
    unittest.main()

