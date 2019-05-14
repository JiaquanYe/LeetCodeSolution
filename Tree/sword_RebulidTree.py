class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def rebuildTree(preOrder, inOrder):
    if len(preOrder) == 0:
        return None
    elif len(preOrder) == 1:
        return TreeNode(preOrder[0])
    else:
        root = TreeNode(data = preOrder[0])
        for idx, elem in enumerate(inOrder):
            if elem == root.data:
                break

        left_inOrder = inOrder[:idx]
        left_preOrder = preOrder[1:idx+1]
        right_inOrder = inOrder[idx+1:]
        right_preOrder = preOrder[idx+1:]

        root.left = rebuildTree(left_preOrder, left_inOrder)
        root.right = rebuildTree(right_preOrder, right_inOrder)

    return root


if __name__ ==  "__main__":
    preOrder = [1,2,4,7,3,5,6,8]
    inOrder = [4,7,2,1,5,3,8,6]
    root = rebuildTree(preOrder, inOrder)
