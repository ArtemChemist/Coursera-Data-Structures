# python3
from collections import deque

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [deque([]) for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        i=0
        for c in s:
            ans = ans + ord(c)*self._multiplier**i
            i+=1
        ans = ans % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            print(*self.elems[query.ind])
        else:
            #figure out hash tag
            tag = self._hash_func(query.s)
            #see if this string is already in database
            in_DB = query.s in self.elems[tag]

            if query.type == 'find':
                if query.s not in self.elems[tag]: 
                    print('no')
                else:
                    print('yes')

            elif query.type == 'add':
                if not in_DB:
                     self.elems[tag].appendleft(query.s)

            elif query.type == 'del':
                if in_DB:
                    self.elems[tag].remove(query.s)
            else:
                pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
