I have implemented a BST in my Python E-Commerce Backend to manage sorted Product IDs, including handling duplicates. I need help generating comprehensive units tests for insertion, searching, deletion and duplicate counting to ensure the code's reliability for real-time inventory updates. Specifically, the tests should verify:

Inserting into an empty tree to check root initialization.
Inserting both unique and duplicate Product IDs to ensure they are correctly added and counts are updated.
Deleting nodes with no children, one child and two children.
Deleting non-existent Product IDs.
Searching for existing and non-existing Product IDs in empty and populated trees.
Here is my BST:

