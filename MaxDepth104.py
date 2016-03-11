# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if(root == None):
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    s = Solution()
    n1= TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n1.left=n2
    n1.right=n3
    print(s.maxDepth(n1))