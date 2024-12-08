# 트리 순회
# Python으로 트리를 쉽게 구현하는 방법: Dictionary 사용
import sys

n = int(sys.stdin.readline())
tree = dict()

for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = [left, right]

# 전위 순회: 루트 -> 왼쪽 자식 -> 오른쪽 자식
def preorder(root):
    if root != '.':
        print(root, end='') # 루트
        preorder(tree[root][0]) # 왼쪽 자식
        preorder(tree[root][1]) # 오른쪽 자식

# 중위 순회: 왼쪽 자식 -> 루트 -> 오른쪽 자식
def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # 왼쪽 자식
        print(root, end='') # 루트
        inorder(tree[root][1]) # 오른쪽 자식

# 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 루트
def postorder(root):
    if root != '.':
        postorder(tree[root][0]) # 왼쪽 자식
        postorder(tree[root][1]) # 오른쪽 자식
        print(root, end='') # 루트
        
preorder('A')
print()
inorder('A')
print()
postorder('A')
