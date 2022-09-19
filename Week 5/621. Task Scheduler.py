import collections
import heapq
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
count = collections.Counter(tasks)
print(count)
maxHeap = [-cnt for cnt in count.values() ]
heapq.heapify(maxHeap)
print(maxHeap)

        