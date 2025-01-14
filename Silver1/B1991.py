# 트리 순회
# Python으로 트리를 쉽게 구현하는 방법: Dictionary 사용
# map을 사용하지 않아도, 공백을 기준으로 값을 나눌 수 있다.
import sys

n = int(sys.stdin.readline())
tree = dict()

for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
