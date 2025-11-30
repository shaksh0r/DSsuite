from DSsuite.BinarySearchTree.BST import BST

def test_remove_root():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    bst.remove(10)

    result = list(bst.in_order())
    # ensure it's sorted and contains the expected elements
    assert result == [5, 15]
    assert result == sorted(result)

test_remove_root()