#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True

class Node:
  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right

class BinaryTree:
  nodes = []

  isBST = True

  def __init__(self):
    self.nodes = []
    self.isBST = True
  
  def read(self, inpt):
    for i in inpt:
      self.nodes.append(Node(i[0],i[1],i[2]))
    if len(self.nodes) == 0:
      isBST = True


  def IsBST(self, current):
    if self.isBST:
      return True
    Right_Is = False
    Right_Is = False
    
    if self.nodes[current].left != -1:
      Left_Is = self.IsBST(self.nodes[current].left)
      Left = self.nodes[self.nodes[current].left]
      Left_Is = Left_Is and (Left.key<self.nodes[current].key)
    else:
      Left_Is = True

    if self.nodes[current].right != -1:
      Right_Is = self.IsBST(self.nodes[current].right)
      Right = self.nodes[self.nodes[current].right]
      Right_Is = Right_Is and (Right.key>self.nodes[current].key)
    else:
      Right_Is = True

    return Left_Is and Right_Is





def main():
  tree = BinaryTree()
  nodes = int(sys.stdin.readline().strip())
  data = []
  for i in range(nodes):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
  if (len(data)>0):
    tree.read(data)

  if tree.IsBST(0):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
