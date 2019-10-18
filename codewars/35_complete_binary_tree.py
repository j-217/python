def complete_binary_tree(a):
    def in_order(n=0):
        if n < len(a):
            yield from in_order(2 * n + 1)
            yield n
            yield from in_order(2 * n + 2)
    result = [None] * len(a)
    for i, x in zip(in_order(), a):
        result[i] = x
    print(result)
    return result


# class TreeNode:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def inorder(self):
#         if self.left:
#             yield from self.left.inorder()
#         yield self
#         if self.right:
#             yield from self.right.inorder()
#
#
# class BinaryCompleteTree:
#     def __init__(self, length):
#         nodes = [TreeNode()]
#         current_idx = 0
#         while len(nodes) < length:
#             node = nodes[current_idx]
#             if node.left is None:
#                 node.left = TreeNode()
#                 nodes.append(node.left)
#             else:
#                 node.right = TreeNode()
#                 nodes.append(node.right)
#                 current_idx += 1
#         self.root = nodes[0]
#         self.bfs = nodes
#
#
# def complete_binary_tree(array):
#     tree = BinaryCompleteTree(len(array))
#     for node, value in zip(tree.root.inorder(), array):
#         node.value = value
#     print([node.value for node in tree.bfs])
#     return [node.value for node in tree.bfs]


complete_binary_tree([1, 2, 3, 4, 5, 6])
