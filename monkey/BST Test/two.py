import unittest

class TestProductIDBST(unittest.TestCase):

    def setUp(self):
        self.bst = ProductIDBST()

    def test_insert_empty_tree(self):
        self.bst.insert(10)
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.count, 1)

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
        self.bst.insert(10)
        self.bst.insert(10)
        self.assertEqual(self.bst.root.key, 10)
        self.assertEqual(self.bst.root.count, 3)

    def test_delete_no_children(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.delete(5)
        self.assertEqual(self.bst.root.key, 10)
        self.assertIsNone(self.bst.root.left)

    def test_delete_one_child(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.delete(15)
        self.assertIsNone(self.bst.root.right)

        self.bst.delete(5)  
        self.assertEqual(self.bst.root.key, 10)
        self.assertIsNone(self.bst.root.left)


    def test_delete_two_children(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(12)
        self.bst.insert(18)
        self.bst.delete(15)
        self.assertEqual(self.bst.root.right.key, 18)
        self.assertEqual(self.bst.root.right.left.key, 12)

    def test_delete_nonexistent_key(self):
        self.bst.insert(10)
        self.bst.delete(5) 
        self.assertEqual(self.bst.root.key, 10)

    def test_delete_duplicate_key(self):
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
        found_node = self.bst.find(5)
        self.assertEqual(found_node.key, 5)

    def test_find_nonexisting_key(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertIsNone(self.bst.find(20))


if __name__ == '__main__':
    unittest.main()