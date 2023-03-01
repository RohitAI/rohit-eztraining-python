class btnode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
n1=btnode(45)
n2=btnode(56)
n3=btnode(78)
n4=btnode(22)
n5=btnode(99)
n6=btnode(56)
n7=btnode(44)
n8=btnode(37)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n7
n3.right=n6
n4.left=n8

print("root:",n1.data)
print("lchild of n1:",n1.left.data)
print("rchild of n1:",n1.right.data)

print(".....................................................")

print("node:",n2.data)
print("lchild of n2:",n2.left.data)
print("rchild of n2:",n2.right.data)

print(".....................................................")
print("node:",n3.data)
print("lchild of n3:",n3.left.data)
print("rchild of n3:",n3.right.data)

print(".....................................................")
print("node:",n4.data)
print("lchild of n4:",n4.left.data)

