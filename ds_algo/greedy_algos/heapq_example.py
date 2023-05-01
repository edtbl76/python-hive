#!/usr/bin/env python3
import heapq

heap = [(0, 'A')]
heapq.heappush(heap, (1, 'B'))
heapq.heappush(heap, (-5, 'D'))
heapq.heappush(heap, (4, 'E'))
heapq.heappush(heap, (2, 'C'))

print("The smallest values in the heap in ascending order are:\n")
while heap:
    print(heapq.heappop(heap))
