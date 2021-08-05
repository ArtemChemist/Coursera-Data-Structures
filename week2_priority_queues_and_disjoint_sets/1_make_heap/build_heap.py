# python3
class Heap:
    size = 0
    data = []
    swaps = []
    
    def __init__(self, s, dt):
        self.size = s
        self.data = dt

    def build_heap(self):
        #Build a heap from ``data`` inplace.
        #Returns a sequence of swaps performed by the algorithm.
        i  = len(self.data)//2
        while (i >= 0):
            self.SiftDown(i)
            i-=1

    def SiftDown(self, i):
        Index = i
        LeftChildIndex = 2*i+1
        RightChildIndex = 2*i+2
        if LeftChildIndex < self.size and self.data[LeftChildIndex] < self.data[Index ]:
            Index = LeftChildIndex
        if RightChildIndex < self.size and self.data[RightChildIndex] < self.data[Index ]:
            Index = RightChildIndex
        if i != Index:
            self.Swap (i, Index)
            self.SiftDown(Index)

    def Swap (self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]
        self.swaps.append((a,b))





def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    hp = Heap(n, data)
    hp.build_heap()
    swaps = hp.swaps

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
