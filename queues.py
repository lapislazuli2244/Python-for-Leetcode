from collections import deque

queue =  deque()

queue.append(1)
queue.append(2)
queue.append(3)

print()
print("After Append: ", queue)

pop_val = queue.pop()
print("After POP: " ,queue)


queue.appendleft(pop_val)
print("After AppendLeft: ", queue)

pop_val = queue.popleft()
print("After PopLeft: ", queue)
