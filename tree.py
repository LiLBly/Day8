class Node:
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild
    
class BinaryTree:
    def __init__(self):
        self.root = None
        self.queue = []

    def level_build_tree(self, data_list):
        """Build a binary tree from a list using level order traversal.

        Args:
            data_list (list): sequence of node values. ``None`` denotes
                the absence of a child.

        Returns:
            Node: root of the constructed binary tree.
        """
        if not data_list:
            return None

        self.root = Node(data_list[0])
        queue = [self.root]
        index = 1

        while queue and index < len(data_list):
            current = queue.pop(0)

            # Assign left child
            if index < len(data_list):
                left_val = data_list[index]
                index += 1
                if left_val is not None:
                    current.lchild = Node(left_val)
                    queue.append(current.lchild)

            # Assign right child
            if index < len(data_list):
                right_val = data_list[index]
                index += 1
                if right_val is not None:
                    current.rchild = Node(right_val)
                    queue.append(current.rchild)

        return self.root