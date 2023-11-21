import sys

input = sys.stdin.readline

n = int(input())

trees={}
for _ in range(n):
    root, node1, node2 = input().split()

    if node1 =='.' and node2=='.':
        trees[root]=[]
        continue
    
    if node1!='.' and node2=='.':
        trees[root]=[node1]
    elif node1=='.' and node2!='.':
        trees[root]=[node2]
    else:
        trees[root]=[node1, node2]

def preorder(v):
    print(v, end='')
    try:
        inorder(trees[v][0])
    except:
        pass
    try:
        inorder(trees[v][1])
    except:
        pass

def inorder(v):
    try:
        inorder(trees[v][0])
    except:
        pass
    print(v, end='')
    try:
        inorder(trees[v][1])
    except:
        pass
def postorder(v):
    try:
        inorder(trees[v][0])
    except:
        pass
    try:
        inorder(trees[v][1])
    except:
        pass
    print(v, end='')
    
preorder('A')
print()
inorder('A')
print()
postorder('A')


#######################

import sys
input = sys.stdin.readline
n = int(input())

inputs = []
for _ in range(n):
    inputs.append(input().split())

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node):
    print(node.item, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
        
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end = '')
    if node.right != '.':
        inorder(tree[node.right])
        
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end = '')

tree = {}
for item, left, right in inputs:
    tree[item] = Node(item, left, right)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])