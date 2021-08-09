# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right

class TreeOrders:
  nodes = []
  result = []

  def read(self):
    self.n = int(sys.stdin.readline())
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.nodes.append(Node(a,b,c))


  def inOrder(self, current):
    if current == -1:
      return
    self.inOrder(self.nodes[current].left)
    self.result.append(self.nodes[current].key)
    self.inOrder(self.nodes[current].right)

    return self.result

  def preOrder(self,current):
    if current == -1:
      return
    self.result.append(self.nodes[current].key)
    self.preOrder(self.nodes[current].left)
    self.preOrder(self.nodes[current].right)
    
    return self.result

  def postOrder(self, current):
    if current == -1:
      return
    self.postOrder(self.nodes[current].left)
    self.postOrder(self.nodes[current].right)
    self.result.append(self.nodes[current].key)
    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(0)))
    tree.result.clear()
    print(" ".join(str(x) for x in tree.preOrder(0)))
    tree.result.clear()
    print(" ".join(str(x) for x in tree.postOrder(0)))
    tree.result.clear()

#if __name__ == '__main__':
#  main()
threading.Thread(target=main).start()
