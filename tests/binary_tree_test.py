from api.models.BinaryTree import BinaryTree


def test_add_and_find_element():
    
    tree = BinaryTree()
    tree.insert(8)
    tree.insert(3)
    tree.insert(6)
    tree.insert(1)
    tree.insert(10)
    tree.insert(14)
    tree.insert(13)
    tree.insert(4)
    tree.insert(7)
    
    assert tree.find(10)
    assert tree.find(3)
    assert tree.find(13)

def test_delete_element():
    
    tree = BinaryTree()
    tree.insert(8)
    tree.insert(3)
    tree.insert(6)
    tree.insert(1)
    tree.insert(10)
    tree.insert(14)
    tree.insert(13)
    tree.insert(4)
    tree.insert(7)
    
    tree.delete(1)
    assert tree.find(1) is False
    
    tree.delete(13)
    assert tree.find(13) is False


def test_inorder_tree():

    tree = BinaryTree()
    tree.insert(8)
    tree.insert(3)
    tree.insert(6)
    tree.insert(1)
    tree.insert(10)
    tree.insert(14)
    tree.insert(13)
    tree.insert(4)
    tree.insert(7)

    assert tree.inorder_list() == [1, 3, 4, 6, 7, 8, 10, 13, 14]

