# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Heap_of_Workers:
    size = 0
    data = []

    
    def __init__(self, Number_of_Threads):
        self.size = Number_of_Threads
        for i in range (0, self.size):
            self.data.append((i,0))
        k = self.size//2
        while k>=0:
            self.SiftDown(k)
            k-=1

    def AddJob(self, JobValue):
        self.data[0] = (self.data[0][0],self.data[0][1]+JobValue)
        self.SiftDown(0)
        pass

    def NextAvailableThread(self):
        return self.data[0][0]
    def Wait_time(self):
        return self.data[0][1]

    def SiftDown(self, i):
        # Index - the index in the array that stores the heap.
        # ID - the original ID of the thread when the heap was created.
        # Value - the sum of all job processed by the thread so far. The thread with the least job processed gets the next job

        Index = i                           #Index that is being processed now
        i_ID = self.data[Index ][0]         #ID of the thread that is being processed now
        i_Val = self.data[Index][1]         #Value for the current thread
        LeftInd = 2*i+1                     #Index of the left child 
        RightInd = 2*i+2                    #Index of the right child


        #Look at the left child. If its value is less, or it has the same value, but lower ID - mark it for swaping
        if LeftInd < self.size:
            LeftID = self.data[LeftInd][0]      #ID of the thread that happened to be the lefty child
            LeftVal = self.data[LeftInd][1]     #Value for the left thread 
            if LeftVal < i_Val:
                Index = LeftInd
            if LeftVal == i_Val and LeftID < i_ID:
                Index = LeftInd

        #Look at the right child. If its value is less, or it has the same value, but lower ID - mark it for swaping
        if RightInd < self.size:
            RightID = self.data[RightInd][0]    #ID of the thread that happened to be the right child
            RightVal = self.data[RightInd][1]   #Value for right thread 
            #Keep in mind that Index could be updated on the comparision with Left
            if RightVal < self.data[Index][1]:
                Index = RightInd
            if RightVal == self.data[Index][1] and RightID < self.data[Index ][0]:
                Index = RightInd

        #If anything is marked for swaping, do the swap and make a recursive call 
        if i != Index:
            self.Swap (i, Index)
            self.SiftDown(Index)

    def Swap (self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]



def assign_jobs(threads:Heap_of_Workers, jobs):
    result = []
    for job in jobs:
        result.append((threads.NextAvailableThread(), threads.Wait_time()))
        threads.AddJob(job)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    threads = Heap_of_Workers(n_workers)

    assigned_jobs = assign_jobs(threads, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
