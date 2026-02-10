queue=[6,9,5,3,4,8]
print("original queue is:",queue)
queue.append(7)
print("queue after pushing the operation:",queue)
queue.pop(0)
print("stack after poping the operation:",queue)
last_element_index=len(queue)-1
print("value obtaiined after peep operation is:",queue[last_element_index])
