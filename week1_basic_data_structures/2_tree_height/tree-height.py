# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
        nodes = []
        def read(self):
                self.n = int(sys.stdin.readline())
                self.input_list = list(map(int, sys.stdin.readline().split()))
                for ID, ParentID in enumerate(self.input_list):
                        nd = Node(ID, ParentID, self)
                        if ParentID == -1:
                                nd.level = 1
                        self.nodes.append(nd)



        def compute_height(self):
                maxHeight = 0
                for nd in self.nodes:
                        if nd.GetLevel() > maxHeight:
                                maxHeight = nd.GetLevel()
                return maxHeight

class Node:
        def __init__(self, ID, parent_ID, ParentTree:Tree):
                self.parent = parent_ID
                self.ID = ID
                self.level = -1
                self.Tree = ParentTree

        def GetLevel(self):
                if self.level >=0:
                        return self.level
                else:
                        try:
                                self.level = self.Tree.nodes[self.parent].GetLevel()+1
                        except:
                                if self.parent == -1:
                                        self.level = 1
                        return self.level
                
def main():
  tree = Tree()
  tree.read()
  print(tree.compute_height())

#if __name__ == "__main__":
#    main()

threading.Thread(target=main).start()
