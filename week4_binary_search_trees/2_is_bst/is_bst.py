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

  def __init__(self):
    self.nodes = []
    self.result = []
    self.isBST = True
    self.size = 0
  
  def read(self, inpt):
    for i in inpt:
      self.nodes.append(Node(i[0],i[1],i[2]))
      self.size+=1
    if len(self.nodes) == 0:
      self.isBST = True

  def inOrder(self, current):
    if current == -1:
      return
    self.inOrder(self.nodes[current].left)
    self.result.append(self.nodes[current].key)
    self.inOrder(self.nodes[current].right)

    return self.result


  def Set_BST_Propety(self, current):
    if current == -1:
      return 
    self.Set_BST_Propety(self.nodes[current].left)
    self.result.append(self.nodes[current].key)
    if len(self.result)>1:
      self.isBST = self.isBST and (self.result[-1]>self.result[-2])
    elif self.size == 1:
      self.isBST
    self.Set_BST_Propety(self.nodes[current].right)

    return 


def main():
  tree = BinaryTree()
  nodes = int(sys.stdin.readline().strip())
  data = []
  for i in range(nodes):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
  if (len(data)>0):
    tree.read(data)
    tree.Set_BST_Propety(0)
  if tree.isBST:
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
