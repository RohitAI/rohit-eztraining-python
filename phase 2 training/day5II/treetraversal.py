class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end="---")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data,end="---")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end="--- ")

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print("preorder:")
preorder(root)
print()
print("postorder:")
postorder(root)
print()
print("inorder:")
inorder(root)
        


##############
#types of BT
1.full                     -  consists of either 2 or 0 child
2.degenrate         -   consists of either 1 or 0 child
3.Scew                 -   consists of either left side or right side  / or \

4.complete          - 1.Every level should be full
                            2. In last level if it is incomplete nodes should be presented at extreme left side
5.perfect           -1. All internal nodes which has 2 child
                          2.leaf nodes both should be at same level
6.balanced        - For all the nodes height of left subtree - height of right subtree can be 0 or 1


BST
All the left side elements should be lesse than its parent
All the right side elements shoulld be greater than its parent



80,10,15,16,45,0,92,73,44,
200,25,5,10,15,-10,-30,61,97,-88,-55,77
