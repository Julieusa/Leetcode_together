def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
      
      
# when A,B=B,A it is different than A=B, B=A, because the first one assigned together, while the second one will replace the value after the first assign.

#or
def invertTree(self, root):
    if root:
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
