#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True

class Node:
  def __init__(self, key, left, right, ID):
    self.key = key
    self.left = left
    self.right = right
    self.ID = ID
    self.BST_here = True



class BinaryTree:

  def __init__(self):
    self.nodes = []
    self.result = []
    self.ID_Tracker = []
    self.isBST = True
    self.size = 0
    self.counter = 0
  
  def read(self, inpt):
    for i in range (0, len(inpt)):
      self.nodes.append(Node(inpt[i][0],inpt[i][1],inpt[i][2],i))
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
      self.GetMaxMin(0)
      return self.isBST 

  def GetMaxMin(self, current):
    maxima = [self.nodes[current].key]
    minima = [self.nodes[current].key]
    if self.nodes[current].left != -1:
        LeftMax, LeftMin = self.GetMaxMin(self.nodes[current].left)
        self.isBST = self.isBST and ( LeftMax < self.nodes[current].key )
        maxima.append(LeftMax)
        minima.append(LeftMin)
        
    if self.nodes[current].right != -1:
        RightMax, RightMin = self.GetMaxMin(self.nodes[current].right)
        self.isBST = self.isBST and ( RightMin >= self.nodes[current].key )
        maxima.append(RightMax)
        minima.append(RightMin)
    
    return max(maxima), min(minima)


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
