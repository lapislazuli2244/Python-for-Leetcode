
import heapq

print()

minHeap = []
heapq.heappush(minHeap, 11)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 22)

print(minHeap)
print()

print("MIN_HEAP")
while(len(minHeap)):
    print(heapq.heappop(minHeap))
    
print()
print("MAX_HEAP")
maxHeap = []
heapq.heappush(maxHeap, -1 * 5)
heapq.heappush(maxHeap, -1 * 4)
heapq.heappush(maxHeap, -1 * 1)
# now while popping multiply it with -1 to get maxHeap

while(len(maxHeap)):
    print(heapq.heappop(maxHeap) * -1)
 
print()

print("Heapify")   
data = [22,444,34,1,3,8,55,23]
heapq.heapify(data)
print(data)