# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append("null")
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        while queue:
            curr = queue.popleft()
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                queue.append(curr.left)
            
            i += 1
            if nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                queue.append(curr.right)
            i += 1

        return root
