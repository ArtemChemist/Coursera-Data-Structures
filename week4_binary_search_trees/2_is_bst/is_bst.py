#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True

class Node:
  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right


class BinaryTree:

  def __init__(self):
    self.nodes = []
    self.result = []
    self.isBST = True
    self.size = 0
    self.counter = 0
  
  def read(self, inpt):
    for i in inpt:
      self.nodes.append(Node(i[0],i[1],i[2]))
      self.size+=1

  def inOrder(self, current):
    if current == -1:
      return
    self.inOrder(self.nodes[current].left)
    self.result.append(self.nodes[current].key)
    self.inOrder(self.nodes[current].right)

    return self.result

  def GetBST(self):
    if self.size<2:
      return True
    else:
      self.Set_BST(0)
      return self.isBST 

  def Set_BST(self, current):
    if current == -1:
      return 
    self.Set_BST(self.nodes[current].left)
    self.result.append(self.nodes[current].key)
    self.counter +=1
    if self.counter>1:
      self.isBST = self.isBST and (self.result[-1]>self.result[-2])
    self.Set_BST(self.nodes[current].right)

    return 


def main():
  tree = BinaryTree()
  nodes = int(sys.stdin.readline().strip())
  data = []
  for i in range(nodes):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
  if (len(data)>0):
    tree.read(data)

  if tree.GetBST():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
